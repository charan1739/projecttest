from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.heading = (By.TAG_NAME, "h1")
        self.description = (By.TAG_NAME, "p")
        self.find_jobs_button = (By.CLASS_NAME, "find-jobs-button")

    def get_heading_text(self):
        return self.driver.find_element(*self.heading).text

    def get_description_text(self):
        return self.driver.find_element(*self.description).text

    def click_find_jobs(self):
        self.driver.find_element(*self.find_jobs_button).click()