"""Required fields on the login form."""
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage

pytestmark = pytest.mark.ui


def test_login_empty_form_shows_email_and_password_errors(page):
    """Goal: the login form validates both required fields.
    Precondition: an empty form in a fresh browser context.
    Expected: Email is required and Password is required are displayed."""
    login = LoginPage(page).open()
    login.submit_button.click()
    expect(login.email_error).to_have_text("Email is required")
    expect(login.password_error).to_have_text("Password is required")
