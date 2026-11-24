"""BDD scenario for the shopping cart business flow using pytest-bdd and page objects."""
import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.home_page import HomePage

pytestmark = [pytest.mark.bdd, pytest.mark.ui]

scenarios("cart.feature")


@given("I am on the home page", target_fixture="home")
def home(page):
    home_page = HomePage(page).open()
    expect(home_page.product_names.first).to_be_visible()
    return home_page


@when(parsers.parse('I open the product "{product}"'), target_fixture="product_page")
def open_product(home, product):
    product_page = home.open_product(product)
    expect(product_page.name).to_have_text(product)
    expect(product_page.unit_price).to_be_visible()
    return product_page


@when(parsers.parse("I add it to the cart with quantity {quantity:d}"), target_fixture="unit_price")
def add_to_cart(product_page, quantity):
    unit = product_page.price()
    product_page.add_to_cart(quantity=quantity)
    expect(product_page.cart_quantity).to_have_text(str(quantity))
    return unit


@when("I open the shopping cart", target_fixture="cart_page")
def open_cart(product_page):
    return product_page.go_to_cart()


@then(parsers.parse('the cart contains "{product}" with quantity {quantity:d}'))
def cart_contains_product(cart_page, product, quantity):
    expect(cart_page.product_titles).to_have_text([product])
    expect(cart_page.quantities).to_have_value(str(quantity))


@then(parsers.parse("the cart line price and total equal the unit price times {quantity:d}"))
def cart_prices_match(cart_page, unit_price, quantity):
    expect(cart_page.line_prices).to_have_count(1)
    expected = unit_price * quantity
    totals = cart_page.line_totals()
    assert totals == pytest.approx([expected]), totals
    assert cart_page.total_value() == pytest.approx(expected)
