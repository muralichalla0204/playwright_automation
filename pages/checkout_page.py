from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def fill_first_name(self, first_name):
        self.page.locator('[data-test="firstName"]').fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator('[data-test="lastName"]').fill(last_name)

    def fill_postal_code(self, postal_code):
        self.page.locator('[data-test="postalCode"]').fill(postal_code)

    def click_continue(self):
        self.page.locator('[data-test="continue"]').click()

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
        self.click_continue()