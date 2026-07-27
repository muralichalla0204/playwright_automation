from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USERNAME, PASSWORD


def test_add_backpack_to_cart(page):

    login = LoginPage(page)

    inventory = InventoryPage(page)

    # Login
    login.login(USERNAME, PASSWORD)

    # Add Backpack
    inventory.add_product_to_cart("sauce-labs-backpack")

    # Verify Remove button
    inventory.verify_remove_button("sauce-labs-backpack")

    # Verify Cart Badge
    inventory.verify_cart_badge(1)