import pytest
from tests.pages.login_page import LoginPage
from tests.pages.navigation_page import NavigationPage
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    # Validate login success
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")


def test_logout_session(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    navigation_page = NavigationPage(page)
    navigation_page.logout()

    # Try to go inventory page after logout
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/")
    

