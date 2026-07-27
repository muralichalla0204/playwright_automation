from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

from utils.test_data import USERNAME, PASSWORD


def test_complete_checkout(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    overview = CheckoutOverviewPage(page)
    complete = CheckoutCompletePage(page)

    # Login
    login.login(USERNAME, PASSWORD)

    # Add product
    inventory.add_product_to_cart("sauce-labs-backpack")
    inventory.verify_cart_badge(1)

    # Open cart
    cart.open_cart()
    cart.verify_cart_url()
    cart.verify_product_visible("Sauce Labs Backpack")
    cart.click_checkout()

    # Checkout information
    checkout.enter_checkout_information(
        "Murali",
        "Challa",
        "500001"
    )

    # Overview
    overview.verify_overview_page()
    overview.click_finish()

    # Complete
    complete.verify_order_successful()
    complete.click_back_home()