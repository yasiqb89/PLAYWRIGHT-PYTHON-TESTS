import re
from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.remove_from_cart = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    def add_item_to_cart(self):
        "Adds product to cart"
        self.add_to_cart.click()
    
    def remove_item_from_cart(self):
        "Remoces a product from cart"
        self.remove_from_cart.click()
    
    def open_cart(self):
        "Click on cart button to cart page"
        self.cart_button.click()
    