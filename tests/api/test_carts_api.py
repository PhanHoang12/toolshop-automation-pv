"""A function-scoped cart created and checked through POST and GET."""
import pytest

pytestmark = pytest.mark.api


@pytest.fixture
def new_cart(api):
    """Create a separate cart for each test that requests this fixture."""
    response = api.post('/carts')
    assert response.status == 201, response.text()
    return response.json()['id']


def test_cart_add_product_quantity_two_is_stored(api, new_cart):
    """Goal: cart API stores the quantity.
    Precondition: a new cart (your fixture) and the first product of GET /products.
    Expected: GET /carts/{id} has exactly 1 item, quantity 2, same product_id."""
    products = api.get('/products', params={'page': 1})
    assert products.status == 200, products.text()
    product = products.json()['data'][0]
    added = api.post(f'/carts/{new_cart}', data={'product_id': product['id'], 'quantity': 2})
    assert added.ok, added.text()
    cart = api.get(f'/carts/{new_cart}')
    assert cart.status == 200, cart.text()
    items = cart.json()['cart_items']
    assert len(items) == 1, items
    assert items[0]['quantity'] == 2, items
    assert str(items[0]['product_id']) == str(product['id']), items
