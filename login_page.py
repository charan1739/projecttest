from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.CLASS_NAME, "login-website-logo")
        self.labels = (By.TAG_NAME, "label")
        self.username_input = (By.ID, "userNameInput")
        self.password_input = (By.ID, "passwordInput")
        self.login_button = (By.CLASS_NAME, "login-button")
        self.error_msg = (By.CLASS_NAME, "error-message")

    def is_logo_displayed(self):
        return self.driver.find_element(*self.logo).is_displayed()

    def get_label_text(self, index):
        return self.driver.find_elements(*self.labels)[index].text

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        time.sleep(1)
        return self.driver.find_element(*self.error_msg).text