import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.checkout_page import CheckoutPage
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
    "Test opening the cart page"
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.open_cart()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")


def test_cart_total_updates_correctly(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_multiple_items_to_cart()
    expect(inventory_page.cart_badge).to_have_text("2")
    inventory_page.cart_button.click()

    checkout_page = CheckoutPage(page, inventory_page)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_shipping_details("Jogn", "Wick", "123")

    # Calculate expected total at checkout step
    expected_total = inventory_page.get_cart_total()
    displayed_total = float(page.locator(".summary_subtotal_label").inner_text().split("$")[1])

    assert expected_total == displayed_total, f"Expected: {expected_total}, Got: {displayed_total}"


def test_cart_persistence_after_navigation(page: Page):
    "Test that cart remembers items after navigating away"
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack.click()

    page.goto("https://www.saucedemo.com/cart.html")

    expect(inventory_page.cart_badge).to_have_text("1")
