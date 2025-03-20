import re
from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.remove_from_cart = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

        self.cart_badge = page.locator("[data-test='shopping-cart-badge']") 
        self.add_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_bike_light = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        
        self.remove_backpack = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.remove_bike_light = page.locator("[data-test='remove-sauce-labs-bike-light']")

        self.item_prices = page.locator(".inventory_item_price") # Get common price locator using inspect element


    def add_item_to_cart(self):
        "Adds product to cart"
        self.add_to_cart.click()
    
    def remove_item_from_cart(self):
        "Remoces a product from cart"
        self.remove_from_cart.click()
    
    def open_cart(self):
        "Click on cart button to cart page"
        self.cart_button.click()
    
    def add_multiple_items_to_cart(self):
        "Add two products to cart"
        self.add_backpack.click()
        self.add_bike_light.click()
    
    def remove_item_from_cart(self):
        "Remove an item from cart"
        self.remove_backpack.click()

    def get_cart_total(self):
        "Calculate total price of items in cart" 
        prices = self.item_prices.all_inner_texts()
        total_price = sum(float(price.replace("$", "")) for price in prices)
        return total_price