import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.checkout_page import CheckoutPage
from playwright.sync_api import Page, expect 

def test_complete_chekout(page:Page):
    "End to End test: Login -> Add item -> Checkout -> Order confirmation"

    page.goto("https://www.saucedemo.com")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart.click()

    checkout_page = CheckoutPage(page, inventory_page)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_shipping_details("John", "Wick", "123")
    checkout_page.complete_checkout()

    expect(checkout_page.order_success_message).to_have_text("Thank you for your order!")
