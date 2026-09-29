from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.config_reader import get_url


class LoginPage(BasePage):
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'
    INVENTORY_CONTAINER = '[data-test="inventory-container"]'

    def __init__(self, page):
        super().__init__(page)

    def open_login_page(self):
        self.open(get_url())

    def login(self, username, password):
        def action():
            self.page.goto(get_url(), wait_until="domcontentloaded")
            self.page.locator(self.USERNAME_INPUT).fill(username)
            self.page.locator(self.PASSWORD_INPUT).fill(password)
            self.page.locator(self.LOGIN_BUTTON).click()

        self._run_step("Login", action)

    def verify_login_success(self):
        self.verify_visible(self.INVENTORY_CONTAINER)
        self.verify_url(f"{get_url()}inventory.html")

    def verify_login_error(self, expected_text):
        def action():
            expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(expected_text)
            expect(self.page).to_have_url(get_url())

        self._run_step("Verify login error", action)

    def verify_login_failure(self):
        def action():
            expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
            expect(self.page).to_have_url(get_url())

        self._run_step("Verify login failure", action)
