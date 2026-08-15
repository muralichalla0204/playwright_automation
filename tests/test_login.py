from pages.login_page import LoginPage
from utils.test_data import (
    INVALID_PASSWORD,
    LOCKED_OUT_USER,
    PASSWORD,
    USERNAME,
)


def test_valid_login(page):
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)
    login.verify_login_success()


def test_locked_out_user_shows_error(page):
    login = LoginPage(page)
    login.login(LOCKED_OUT_USER, PASSWORD)
    login.verify_login_error("Sorry, this user has been locked out.")


def test_invalid_credentials_shows_error(page):
    login = LoginPage(page)
    login.login(USERNAME, INVALID_PASSWORD)
    login.verify_login_error("Username and password do not match")
