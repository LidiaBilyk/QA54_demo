from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_ICON = (By.XPATH, "//a[@class='ico-login']")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")
    LOG_OUT_BUTTON = (By.XPATH, "//a[@class='ico-logout']")
    REMEMBER_ME_BUTTON = (By.ID, "RememberMe")
    WRONG_EMAIL_MESSAGE = (By.XPATH, "//li[normalize-space()='No customer account found']")
    WRONG_PASSWORD_MESSAGE = (By.XPATH, "//li[normalize-space()='The credentials provided are incorrect']")
    INVALID_EMAIL_MESSAGE = (By.XPATH, "//span[@for='Email']")

    def is_login_icon_displayed(self):
        return self.is_element_visible(self.LOGIN_ICON)

    def are_login_form_elements_displayed(self):
        return (self.is_element_visible(self.EMAIL_INPUT)
                and self.is_element_visible(self.PASSWORD_INPUT)
                and self.is_element_visible(self.REMEMBER_ME_BUTTON)
                and self.is_element_visible(self.LOGIN_BUTTON))

    def open_login_page(self):
        self.click_element(self.LOGIN_ICON)

    def fill_email_field(self, email):
        self.input_text(self.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def is_log_out_displayed(self):
        return self.is_element_visible(self.LOG_OUT_BUTTON)

    def is_wrong_email_message(self):
        return self.is_element_visible(self.WRONG_EMAIL_MESSAGE)

    def is_wrong_password_message(self):
        return self.is_element_visible(self.WRONG_PASSWORD_MESSAGE)

    def is_invalid_email_message(self):
        return self.is_element_visible(self.INVALID_EMAIL_MESSAGE)

    def login(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_login_button()