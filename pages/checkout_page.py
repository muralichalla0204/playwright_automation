from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = '[data-test="firstName"]'
    LAST_NAME = '[data-test="lastName"]'
    POSTAL_CODE = '[data-test="postalCode"]'
    CONTINUE_BUTTON = '[data-test="continue"]'

    def __init__(self, page):
        super().__init__(page)

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)
