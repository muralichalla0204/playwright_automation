print("******** conftest.py loaded ********")

import os
import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import get_browser, get_headless


@pytest.fixture
def page():

    browser_name = get_browser()
    headless = get_headless()

    with sync_playwright() as p:

        browser = getattr(p, browser_name).launch(
            headless=headless
        )

        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = f"screenshots/{item.name}.png"

            page.screenshot(path=screenshot_name)

            print(f"\nScreenshot saved: {screenshot_name}")