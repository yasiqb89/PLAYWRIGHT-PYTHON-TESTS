import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.navigation_page import NavigationPage
from playwright.sync_api import Page, expect


def test_navigate_to_all_items(page:Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    navigation_page = NavigationPage(page)
    navigation_page.navigate_to_all_items()

def test_navigate_to_about(page:Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    navigation_page = NavigationPage(page)
    navigation_page.navigate_to_about()
    expect(page).to_have_url("https://saucelabs.com/")


def test_navigate_to_cart(page:Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    navigation_page = NavigationPage(page)
    navigation_page.navigate_to_cart()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")

def test_logout(page:Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    navigation_page = NavigationPage(page)
    navigation_page.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_invalid_product_id_manipulation(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    #Try to navigate using invalid product-id
    page.goto("https://www.saucedemo.com/inventory-item.html?id=9999")

    expect(page.locator(".inventory_details_name")).to_have_text("ITEM NOT FOUND")
    
    navigation_page = NavigationPage(page)
    expect(navigation_page.back_to_products_button).to_be_visible()





