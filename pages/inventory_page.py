from playwright.sync_api import expect
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def add_product_to_cart(self, product):
        self.page.locator(
            f'[data-test="add-to-cart-{product}"]'
        ).click()

    def verify_remove_button(self, product):
        expect(
            self.page.locator(
                f'[data-test="remove-{product}"]'
            )
        ).to_be_visible()

    def verify_cart_badge(self, count):
        expect(
            self.page.locator(
                '[data-test="shopping-cart-badge"]'
            )
        ).to_have_text(str(count))