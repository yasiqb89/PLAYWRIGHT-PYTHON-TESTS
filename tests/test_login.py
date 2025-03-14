import pytest
from tests.pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    # Validate login success
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")
