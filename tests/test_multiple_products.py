from pages.inventory_page import InventoryPage
from utils.test_data import PRODUCTS


def test_add_multiple_products(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    for product in PRODUCTS:
        inventory.add_product_to_cart(product)
        inventory.verify_remove_button(product)

    inventory.verify_cart_badge(len(PRODUCTS))
