from playwright.sync_api import expect
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def verify_cart_url(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")

    from playwright.sync_api import expect

    def verify_product_visible(self, product_name):
        expect(
        self.page.locator('[data-test="inventory-item-name"]')
                ).to_have_text(product_name)

    def click_checkout(self):
        self.page.locator('[data-test="checkout"]').click()