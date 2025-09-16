from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class JobsPage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_img = (By.CSS_SELECTOR, "img.profile-img")
        self.profile_name = (By.CLASS_NAME, "profile-name")
        self.profile_bio = (By.CLASS_NAME, "short-bio")
        self.search_input = (By.XPATH, "/html/body/div/div/div/div/div[3]/div/div/div/input")
        self.search_button = (By.XPATH, "/html/body/div/div/div/div/div[1]/div/div/button")
        self.job_cards = (By.CLASS_NAME, "link-item")
        self.no_jobs_img = (By.CLASS_NAME, "jobs-not-found-img")
        self.no_jobs_heading = (By.CLASS_NAME, "jobs-not-found-heading")
        self.no_jobs_description = (By.CLASS_NAME, "jobs-not-found-description")

    def is_profile_img_displayed(self):
        WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located(self.profile_img)
    )
        return self.driver.find_element(*self.profile_img).is_displayed()

    def get_profile_name(self):
        return self.driver.find_element(*self.profile_name).text

    def get_profile_bio(self):
        return self.driver.find_element(*self.profile_bio).text

    def enter_search_text(self, text):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.search_input))
        search_box = self.driver.find_element(*self.search_input)
        search_box.find_element(*self.search_input).clear()
        search_box.find_element(*self.search_input).send_keys(text)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def search_job(self, text):
        self.enter_search_text(text)
        self.click_search()

    def get_jobs_count(self):
        return len(self.driver.find_elements(*self.job_cards))

    def is_no_jobs_img_displayed(self):
        return self.driver.find_element(*self.no_jobs_img).is_displayed()

    def get_no_jobs_heading(self):
        return self.driver.find_element(*self.no_jobs_heading).text

    def get_no_jobs_description(self):
        return self.driver.find_element(*self.no_jobs_description).text
