from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utils.test_data import CHECKOUT_INFO


def test_complete_checkout(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)
    overview = CheckoutOverviewPage(logged_in_page)
    complete = CheckoutCompletePage(logged_in_page)

    inventory.add_product_to_cart("sauce-labs-backpack")
    inventory.verify_cart_badge(1)

    cart.open_cart()
    cart.verify_cart_url()
    cart.verify_product_visible("Sauce Labs Backpack")
    cart.click_checkout()

    checkout.enter_checkout_information(
        CHECKOUT_INFO["first_name"],
        CHECKOUT_INFO["last_name"],
        CHECKOUT_INFO["postal_code"],
    )

    overview.verify_overview_page()
    overview.click_finish()

    complete.verify_order_successful()
    complete.click_back_home()
