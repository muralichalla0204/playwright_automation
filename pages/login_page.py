from pages.base_page import BasePage
from utils.config_reader import get_url

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):

        self.open(get_url())

        self.fill('[data-test="username"]', username)

        self.fill('[data-test="password"]', password)

        self.click('[data-test="login-button"]')