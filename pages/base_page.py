from playwright.sync_api import expect

from utils.logger import logger


class BasePage:

    def __init__(self, page):
        self.page = page

    def _recorder(self):
        return getattr(self.page, "_step_recorder", None)

    def _run_step(self, action, callback):
        recorder = self._recorder()
        if recorder:
            return recorder.run_step(action, callback)
        return callback()

    def open(self, url):
        def action():
            logger.info(f"Opening URL: {url}")
            self.page.goto(url)

        self._run_step(f"Open URL: {url}", action)

    def click(self, locator):
        def action():
            logger.info(f"Clicking: {locator}")
            self.page.locator(locator).click()

        self._run_step(f"Click: {locator}", action)

    def fill(self, locator, text):
        def action():
            logger.info(f"Filling {locator}")
            self.page.locator(locator).fill(text)

        self._run_step(f"Fill: {locator}", action)

    def verify_text(self, locator, expected_text):
        def action():
            logger.info(f"Verifying text '{expected_text}' in {locator}")
            expect(self.page.locator(locator)).to_have_text(expected_text)

        self._run_step(f"Verify text '{expected_text}' in {locator}", action)

    def verify_visible(self, locator):
        def action():
            logger.info(f"Verifying element is visible: {locator}")
            expect(self.page.locator(locator)).to_be_visible()

        self._run_step(f"Verify visible: {locator}", action)

    def verify_url(self, expected_url):
        def action():
            logger.info(f"Verifying URL: {expected_url}")
            expect(self.page).to_have_url(expected_url)

        self._run_step(f"Verify URL: {expected_url}", action)

    def verify_contains_text(self, locator, expected_text):
        def action():
            logger.info(f"Verifying text contains '{expected_text}' in {locator}")
            expect(self.page.locator(locator)).to_contain_text(expected_text)

        self._run_step(
            f"Verify contains text '{expected_text}' in {locator}",
            action,
        )

    def get_title(self):
        return self._run_step("Get page title", self.page.title)

    def get_url(self):
        return self._run_step("Get current URL", lambda: self.page.url)
