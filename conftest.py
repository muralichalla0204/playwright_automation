import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.config_reader import get_browser, get_headless
from utils.logger import logger
from utils.step_recorder import StepRecorder
from utils.test_data import PASSWORD, USERNAME


@pytest.fixture
def page(request):
    browser_name = get_browser()
    headless = get_headless()

    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_name).launch(headless=headless)
        context = browser.new_context()
        test_page = context.new_page()

        recorder = StepRecorder(request.node.name, test_page)
        test_page._step_recorder = recorder
        request.node._step_recorder = recorder

        yield test_page

        context.close()
        browser.close()


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)
    login.verify_login_success()
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    recorder = getattr(item, "_step_recorder", None)
    if not recorder:
        return

    test_status = "PASSED" if report.passed else "FAILED"

    if report.failed:
        recorder.record(
            "Test failed — final state",
            "FAILED",
            str(report.longrepr),
        )
        logger.error("Test failed: %s", item.name)

    recorder.finalize(test_status)
