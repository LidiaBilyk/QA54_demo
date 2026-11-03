import os

from dotenv import load_dotenv

from pages.login_page import LoginPage

load_dotenv()

#valid data - user with this email exists and registered, the pass matches the email
VALID_EMAIL = "test_user@gm.com"
VALID_PASSWORD = os.getenv("TEST_USER_PASSWORD")
if not VALID_PASSWORD:
    raise ValueError("Critical error: password not found in the environment!")

#wrong data - unregistered email (valid format), pass (valid format) doesn't match the login
UNREGISTERED_EMAIL = "test1_user1@gm.com"
WRONG_PASSWORD = os.getenv("TEST_USER_WRONG_PASSWORD")
if not WRONG_PASSWORD:
    raise ValueError("Critical error: wrong password not found in the environment!")

#invalid data - invalid format of email
INVALID_EMAIL = "test1gg.com"


def test_login_form_is_available(driver):
    login_page = LoginPage(driver)
    assert login_page.is_login_icon_displayed(), "Login icon not found"
    login_page.open_login_page()
    assert login_page.are_login_form_elements_displayed(), "Login form elements are not displayed"

def test_valid_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    assert login_page.is_log_out_displayed(), "Logout button is not displayed"

def test_with_invalid_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD)
    assert login_page.is_invalid_email_message(), "Invalid Email format message is not displayed"

def test_with_unregistered_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(UNREGISTERED_EMAIL, VALID_PASSWORD)
    assert login_page.is_wrong_email_message(), "Account not found message is not displayed"

def test_with_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(VALID_EMAIL, WRONG_PASSWORD)
    assert login_page.is_wrong_password_message(), "Incorrect credentials message is not displayed"