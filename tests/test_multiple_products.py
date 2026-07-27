from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USERNAME, PASSWORD

def test_add_multiple_products(page):

    # Create page objects
    login = LoginPage(page)
    inventory = InventoryPage(page)

    # Login
    login.login(USERNAME, PASSWORD)

    # Products to add
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ]

    # Add each product
    for product in products:
        inventory.add_product_to_cart(product)
        inventory.verify_remove_button(product)

    # Verify cart badge
    inventory.verify_cart_badge(len(products))