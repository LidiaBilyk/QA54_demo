from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    LOGIN_ICON = (By.XPATH, "//a[@class='ico-login']")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")
    LOG_OUT_BUTTON = (By.XPATH, "//a[@class='ico-logout']")
    REMEMBER_ME_BUTTON = (By.ID, "RememberMe")
    WRONG_EMAIL_MESSAGE = (By.XPATH, "//li[normalize-space()='No customer account found']")
    WRONG_PASSWORD_MESSAGE = (By.XPATH, "//li[normalize-space()='The credentials provided are incorrect']")
    INVALID_EMAIL_MESSAGE = (By.XPATH, "//span[@for='Email']")

    def __init__(self, driver):
        self.driver = driver

    def is_login_icon_displayed(self):
        return self.driver.find_element(*self.LOGIN_ICON).is_displayed()

    def are_login_form_elements_displayed(self):
        email_visible = self.driver.find_element(*self.EMAIL_INPUT).is_displayed()
        password_visible = self.driver.find_element(*self.PASSWORD_INPUT).is_displayed()
        remember_me_visible = self.driver.find_element(*self.REMEMBER_ME_BUTTON).is_displayed()
        login_btn_visible = self.driver.find_element(*self.LOGIN_BUTTON).is_displayed()

        return email_visible and password_visible and remember_me_visible and login_btn_visible

    def open_login_page(self):
        # self.driver.get(self.LOGIN_LINK).click()
        self.driver.find_element(*self.LOGIN_ICON).click()

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # def is_sign_out_displayed(self):
    #     return self.driver.find_element(*self.SIGN_OUT_BUTTON).is_displayed()

    def is_log_out_displayed(self):
        try:
            WebDriverWait(self.driver, timeout = 10).until(
                expected_conditions.visibility_of_element_located(self.LOG_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    def is_wrong_email_message(self):
        try:
            WebDriverWait(self.driver, timeout = 10).until(
                expected_conditions.visibility_of_element_located(self.WRONG_EMAIL_MESSAGE)
            )
            return True
        except TimeoutException:
            return False

    def is_wrong_password_message(self):
        try:
            WebDriverWait(self.driver, timeout = 10).until(
                expected_conditions.visibility_of_element_located(self.WRONG_PASSWORD_MESSAGE)
            )
            return True
        except TimeoutException:
            return False

    def is_invalid_email_message(self):
        try:
            WebDriverWait(self.driver, timeout = 10).until(
                expected_conditions.visibility_of_element_located(self.INVALID_EMAIL_MESSAGE)
            )
            return True
        except TimeoutException:
            return False