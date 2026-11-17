"""Product details agree with the selected catalogue card."""
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage

pytestmark = pytest.mark.ui


def test_product_details_match_catalogue_name_and_price(page):
    """Goal: the detail page shows the product the shopper selected.
    Precondition: a product card with a name and price is visible.
    Expected: the detail name contains the selected name and the unit price agrees."""
    home = HomePage(page).open()
    expect(home.product_names.first).to_be_visible()
    expect(home.product_prices.first).to_be_visible()
    name = home.product_names.first.inner_text().strip()
    listed_price = home.prices()[0]
    product = home.open_product(name)
    expect(product.name).to_contain_text(name)
    expect(product.unit_price).to_be_visible()
    assert product.price() == pytest.approx(listed_price)
