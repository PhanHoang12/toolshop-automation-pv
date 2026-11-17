"""Catalogue search, price ordering and category filtering."""
import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage

pytestmark = pytest.mark.ui


def test_search_unknown_keyword_shows_empty_state(page):
    """Goal: an unknown keyword has a clear empty state.
    Precondition: the public product catalogue is available.
    Expected: the no-results message appears and there are zero product cards."""
    home = HomePage(page).open().search("zzz-no-such-tool")
    expect(home.search_completed).to_be_visible()
    expect(home.no_results).to_have_text("There are no products found.")
    expect(home.product_names).to_have_count(0)


@pytest.mark.parametrize("order", ["price,asc", "price,desc"])
def test_catalog_sort_by_price_orders_visible_products(page, order):
    """Goal: the catalogue orders prices in the selected direction.
    Precondition: a non-empty product catalogue.
    Expected: displayed prices are sorted ascending or descending as selected."""
    home = HomePage(page).open()
    expect(home.product_names.first).to_be_visible()
    home.sort_by(order)
    expect(home.sorting_completed).to_be_visible()
    prices = home.prices()
    assert prices, "the product grid must not be empty"
    assert prices == sorted(prices, reverse=order == "price,desc"), prices


def test_category_hammer_filter_shows_only_hammers(page):
    """Goal: the Hammer category filters the product catalogue.
    Precondition: the category is available and no filters are selected.
    Expected: Hammer is checked and every returned product name contains hammer."""
    home = HomePage(page).open()
    expect(home.product_names.first).to_be_visible()
    home.filter_hammers()
    expect(home.hammer_category).to_be_checked()
    expect(home.filter_completed).to_be_visible()
    names = home.product_names.all_inner_texts()
    assert names, "the Hammer category returned no products"
    assert all("hammer" in name.lower() for name in names), names
