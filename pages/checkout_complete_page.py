from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    SUCCESS_HEADER = '[data-test="complete-header"]'
    BACK_HOME_BUTTON = '[data-test="back-to-products"]'

    def __init__(self, page):
        super().__init__(page)

    def verify_order_successful(self):
        self.verify_text(self.SUCCESS_HEADER, "Thank you for your order!")

    def click_back_home(self):
        self.click(self.BACK_HOME_BUTTON)
