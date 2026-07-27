from playwright.sync_api import expect
from utils.logger import logger


class BasePage:

    def __init__(self, page):
        self.page = page

    # -------------------
    # Reusable Actions
    # -------------------

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.page.goto(url)

    def click(self, locator):
        logger.info(f"Clicking: {locator}")
        self.page.locator(locator).click()

    def fill(self, locator, text):
        logger.info(f"Filling {locator} with '{text}'")
        self.page.locator(locator).fill(text)

    # -------------------
    # Reusable Verifications
    # -------------------

    def verify_text(self, locator, expected_text):
        logger.info(f"Verifying text '{expected_text}' in {locator}")
        expect(self.page.locator(locator)).to_have_text(expected_text)

    def verify_visible(self, locator):
        logger.info(f"Verifying element is visible: {locator}")
        expect(self.page.locator(locator)).to_be_visible()

    def verify_url(self, expected_url):
        logger.info(f"Verifying URL: {expected_url}")
        expect(self.page).to_have_url(expected_url)

    def get_title(self):
        logger.info("Getting page title")
        return self.page.title()

    def get_url(self):
        logger.info("Getting current URL")
        return self.page.url