"""An authenticated account page reuses the session storage state."""
import pytest
from playwright.sync_api import expect

from pages.account_page import AccountPage

pytestmark = pytest.mark.ui


def test_account_saved_login_shows_own_title_and_user_menu(logged_in_page):
    """Goal: an account page can reuse the session's saved login.
    Precondition: logged_in_page restores storage state for the registered QA Bot.
    Expected: the title is My account and the user menu contains QA Bot."""
    account = AccountPage(logged_in_page).open()
    expect(account.title).to_have_text("My account")
    expect(account.nav_menu).to_contain_text("QA Bot")
