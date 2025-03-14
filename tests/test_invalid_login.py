import pytest
from tests.pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("invalid_user", "wrong_password")
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface")