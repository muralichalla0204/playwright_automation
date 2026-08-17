from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_BADGE = '[data-test="shopping-cart-badge"]'

    def __init__(self, page):
        super().__init__(page)

    def add_product_to_cart(self, product):
        self.click(f'[data-test="add-to-cart-{product}"]')

    def verify_remove_button(self, product):
        self.verify_visible(f'[data-test="remove-{product}"]')

    def verify_cart_badge(self, count):
        self.verify_text(self.CART_BADGE, str(count))
