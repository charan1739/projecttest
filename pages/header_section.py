from selenium.webdriver.common.by import By
import time

class HeaderSection:
    def __init__(self, driver):
        self.driver = driver
        self.logo_img = (By.TAG_NAME, "img")
        self.logo_link = (By.LINK_TEXT, "Home")
        self.nav_home = (By.LINK_TEXT, "Home")
        self.nav_jobs = (By.LINK_TEXT, "Jobs")
        self.logout_button = (By.CLASS_NAME, "logout-desktop-btn")

    def is_logo_displayed(self):
        time.sleep(1)
        return self.driver.find_element(*self.logo_img).is_displayed()

    def click_logo_link(self):
        self.driver.find_element(*self.logo_link).click()

    def click_nav_home(self):
        self.driver.find_element(*self.nav_home).click()

    def click_nav_jobs(self):
        self.driver.find_element(*self.nav_jobs).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.switch_to.default_content()
