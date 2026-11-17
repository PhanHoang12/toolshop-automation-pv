"""Cart quantities and price arithmetic."""
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage

pytestmark = pytest.mark.ui


def test_cart_line_and_total_equal_unit_price_times_quantity(page):
    """Goal: the cart stores the selected quantity and calculates prices correctly.
    Precondition: a fresh empty cart and an available Combination Pliers.
    Expected: quantity 2, line price equal to unit price times 2, and the correct total."""
    product = HomePage(page).open().open_product("Combination Pliers")
    expect(product.name).to_have_text("Combination Pliers")
    unit_price = product.price()
    product.add_to_cart(quantity=2)
    expect(product.cart_quantity).to_have_text("2")
    cart = product.go_to_cart()
    expect(cart.product_titles).to_have_text(["Combination Pliers"])
    expect(cart.quantities).to_have_value("2")
    expect(cart.line_prices).to_have_count(1)
    totals = cart.line_totals()
    assert totals == pytest.approx([unit_price * 2]), totals
    assert cart.total_value() == pytest.approx(sum(totals))
