from pages.base_page import BasePage
from utils.config_reader import get_url


class CartPage(BasePage):
    CART_LINK = '[data-test="shopping-cart-link"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'
    ITEM_NAME = '[data-test="inventory-item-name"]'

    def __init__(self, page):
        super().__init__(page)

    def open_cart(self):
        self.click(self.CART_LINK)

    def verify_cart_url(self):
        self.verify_url(f"{get_url()}cart.html")

    def verify_product_visible(self, product_name):
        self.verify_text(self.ITEM_NAME, product_name)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
