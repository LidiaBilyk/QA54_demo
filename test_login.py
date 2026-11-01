import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

URL = "https://demowebshop.tricentis.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(URL)

    yield driver
    driver.quit()

class TestLogin:

    def test_login_form(self, driver):
        icon = driver.find_element(By.XPATH, "//a[@class='ico-login']")
        assert icon.is_displayed()

        icon.click()

        email_input = driver.find_element(By.ID, "Email")
        assert email_input.is_displayed()

        password_input = driver.find_element(By.ID, "Password")
        assert password_input.is_displayed()

        remember_me_checkbox_input = driver.find_element(By.ID, "RememberMe")
        assert remember_me_checkbox_input.is_displayed()

        login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
        assert login_button.is_displayed()

    def test_login_success(self, driver):
        password = os.getenv("TEST_USER_PASSWORD")
        if not password:
            raise ValueError("Critical error: password not found in the environment!")
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.ID, "Email").send_keys("test_user@gm.com")
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        assert driver.find_element(By.XPATH, "//a[@href='/customer/info']").is_displayed()
        assert driver.find_element(By.XPATH, "//a[@class='ico-logout']").is_displayed()







