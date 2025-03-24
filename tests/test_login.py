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
    

def test_locked_out_user_shows_error_message(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)

    login_page.login("locked_out_user", "secret_sauce")

    # Check for locked-out error message
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")