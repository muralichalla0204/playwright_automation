from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def verify_overview_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-two.html"
        )

    def click_finish(self):
        self.page.locator('[data-test="finish"]').click()