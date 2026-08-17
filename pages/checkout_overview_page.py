from pages.base_page import BasePage
from utils.config_reader import get_url


class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = '[data-test="finish"]'

    def __init__(self, page):
        super().__init__(page)

    def verify_overview_page(self):
        self.verify_url(f"{get_url()}checkout-step-two.html")

    def click_finish(self):
        self.click(self.FINISH_BUTTON)
