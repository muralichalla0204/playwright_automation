from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def verify_order_successful(self):
        expect(
            self.page.locator('[data-test="complete-header"]')
        ).to_have_text("Thank you for your order!")

    def click_back_home(self):
        self.page.locator('[data-test="back-to-products"]').click()