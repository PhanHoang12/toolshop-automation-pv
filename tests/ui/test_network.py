"""Network interception checks, separate from the twelve business UI cases."""
import json
import re

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage, PRODUCT_LIST

pytestmark = [pytest.mark.ui, pytest.mark.route]
EMPTY_PAGE = {
    "current_page": 1, "data": [], "from": None, "last_page": 1,
    "per_page": 9, "to": None, "total": 0,
}


def test_home_without_images_still_lists_products(page):
    """Goal: the catalogue remains usable when images are blocked.
    Precondition: image requests are intercepted before opening the home page.
    Expected: product names visible AND at least one image request was aborted (prove the route ran)."""
    blocked = []

    def block(route):
        blocked.append(route.request.url)
        route.abort()
    page.route(re.compile('\\.(png|jpe?g|webp|avif|svg)(\\?.*)?$', re.IGNORECASE), block)
    home = HomePage(page).open()
    expect(home.product_names.first).to_be_visible()
    assert blocked, 'no image request was blocked'


def test_home_with_empty_product_list_shows_no_results(page):
    """Goal: an empty catalogue is explained to the user.
    Precondition: the product list API is mocked with EMPTY_PAGE.
    Expected: 'There are no products found.' and 0 product cards."""
    page.route(PRODUCT_LIST, lambda route: route.fulfill(status=200, content_type='application/json', body=json.dumps(EMPTY_PAGE)))
    home = HomePage(page).open()
    expect(home.no_results).to_have_text('There are no products found.')
    expect(home.product_names).to_have_count(0)
