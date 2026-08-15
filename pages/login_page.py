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
        self.open_login_page()
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def verify_login_success(self):
        self.verify_visible(self.INVENTORY_CONTAINER)
        self.verify_url(f"{get_url()}inventory.html")

    def verify_login_error(self, expected_message):
        self.verify_visible(self.ERROR_MESSAGE)
        self.verify_contains_text(self.ERROR_MESSAGE, expected_message)
