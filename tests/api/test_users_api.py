"""Registration validation and authenticated profile access."""
import pytest

pytestmark = pytest.mark.api


def test_register_empty_body_returns_422_with_field_errors(api):
    """Goal: required registration fields are validated on the server.
    Precondition: none.
    Expected: 422 and error lists for 'email' and 'password'."""
    response = api.post('/users/register', data={})
    assert response.status == 422, response.text()
    errors = response.json()
    for field in ('email', 'password'):
        assert isinstance(errors.get(field), list) and errors[field], errors


def test_users_me_with_token_returns_own_profile(api, auth_headers, test_user):
    """Goal: a bearer token grants access to the user's own profile.
    Precondition: a user registered and logged in by the shared fixtures.
    Expected: 200 and the same email."""
    response = api.get('/users/me', headers=auth_headers)
    assert response.status == 200, response.text()
    assert response.json()['email'] == test_user['email']
