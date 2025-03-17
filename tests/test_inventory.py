import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from playwright.sync_api import Page, expect

def test_add_item_to_cart(page: Page):
    "Testing adding an item to the cart"
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()


def test_remove_item_from_cart(page: Page):
    "Testing remove item from cart"
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart()
    inventory_page.remove_item_from_cart()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()

def test_open_cart(page: Page):
    """Test opening the cart page"""
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.open_cart()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")