from pages.inventory_page import InventoryPage


def test_add_backpack_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_product_to_cart("sauce-labs-backpack")
    inventory.verify_remove_button("sauce-labs-backpack")
    inventory.verify_cart_badge(1)
