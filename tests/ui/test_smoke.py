"""Sprint 1: four UI smoke tests using page objects."""
import re

import pytest
from playwright.sync_api import expect

from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.ui
def test_search_pliers_returns_only_matching_products(page):
    """Goal: search filters products by keyword.
    Precondition: the public product catalogue is available.
    Expected: results exist and every product name contains pliers."""
    home = HomePage(page).open().search("pliers")
    expect(home.search_completed).to_be_visible()
    expect(home.search_caption).to_contain_text("pliers")
    names = home.product_names.all_inner_texts()
    assert names, "search returned no products"
    assert all("pliers" in name.lower() for name in names), names


@pytest.mark.smoke
@pytest.mark.ui
def test_add_three_claw_hammers_updates_cart_badge(page):
    """Goal: adding a product uses the selected quantity.
    Precondition: an empty cart and an available Claw Hammer.
    Expected: a success toast appears and the cart badge shows 3."""
    product = HomePage(page).open().open_product("Claw Hammer")
    expect(product.name).to_have_text("Claw Hammer")
    product.add_to_cart(quantity=3)
    expect(product.toast).to_contain_text("Product added to shopping cart")
    expect(product.cart_quantity).to_have_text("3")


@pytest.mark.smoke
@pytest.mark.ui
def test_login_unknown_email_shows_error_and_keeps_login_url(page):
    """Goal: invalid credentials are rejected.
    Precondition: an email without an account, never a shared class account.
    Expected: Invalid email or password appears and the URL ends in /auth/login."""
    login = LoginPage(page).open().login("nobody-here@example.com", "Wrong-Password-123")
    expect(login.error).to_contain_text("Invalid email or password")
    expect(page).to_have_url(re.compile(r"/auth/login$"))


@pytest.mark.smoke
@pytest.mark.ui
def test_contact_empty_form_shows_subject_and_message_errors(page):
    """Goal: the contact form validates required fields.
    Precondition: an empty contact form in a fresh browser context.
    Expected: Subject is required and Message is required are displayed."""
    contact = ContactPage(page).open().submit()
    expect(contact.errors).to_contain_text(["Subject is required", "Message is required"])
