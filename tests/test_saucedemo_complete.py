from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import CHECKOUT_INFO, PASSWORD, USERNAME


def test_saucedemo_complete_journey(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    overview = CheckoutOverviewPage(page)
    complete = CheckoutCompletePage(page)

    # Login
    login.login(USERNAME, PASSWORD)
    login.verify_login_success()

    # Inventory
    inventory.verify_visible('[data-test="inventory-list"]')
    inventory.add_product_to_cart("sauce-labs-backpack")
    inventory.verify_cart_badge(1)

    # Cart
    cart.open_cart()
    cart.verify_cart_url()
    cart.verify_product_visible("Sauce Labs Backpack")
    cart.click_checkout()

    # Checkout information
    checkout.verify_visible(CheckoutPage.FIRST_NAME)
    checkout.enter_checkout_information(
        CHECKOUT_INFO["first_name"],
        CHECKOUT_INFO["last_name"],
        CHECKOUT_INFO["postal_code"],
    )

    # Overview and completion
    overview.verify_overview_page()
    overview.click_finish()
    complete.verify_order_successful()