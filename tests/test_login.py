import pytest
from tests.pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    # Validate login success
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")


@pytest.mark.parametrize("username, password, expected_error",[
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")])
def test_login_with_invalid_credentials(page:Page, username, password, expected_error):
    "Testing login page with invalid login credentials"
    page.goto("https://www.saucedemo.com/")
    loging_page = LoginPage(page)
    loging_page.login(username, password)

    #Check error message
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_have_text(expected_error)