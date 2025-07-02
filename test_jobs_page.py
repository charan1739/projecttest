import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login_page import LoginPage
from jobs_page import JobsPage
from home_page import HomePage
import time

@pytest.fixture()
def jobs_page():
    driver = webdriver.Chrome()
    driver.get("https://qajobbyapp.ccbp.tech/login")
    login_page = LoginPage(driver)
    login_page.login("rahul", "rahul@2021")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://qajobbyapp.ccbp.tech/"))
    home_page = HomePage(driver)
    home_page.click_find_jobs()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://qajobbyapp.ccbp.tech/jobs"))
    yield JobsPage(driver)
    driver.quit()

def test_profile_ui(jobs_page):
    time.sleep(2)
    assert jobs_page.is_profile_img_displayed(), "Profile image is not displayed"
    assert jobs_page.get_profile_name() == "Rahul Attluri", "Profile name does not match"
    assert jobs_page.get_profile_bio() == "Lead Software Developer and AI-ML expert", "Bio does not match"

def test_successful_search(jobs_page):
    time.sleep(2)
    jobs_page.search_job("Developer")
    time.sleep(2)
    assert jobs_page.get_jobs_count() > 0, "Jobs count does not match"

def test_unsuccessful_search(jobs_page):
    jobs_page.search_job("Netflix")
    WebDriverWait(jobs_page.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "jobs-not-found-img"))
    )
    assert jobs_page.is_no_jobs_img_displayed(), "Jobs not found image is not displayed"
    assert jobs_page.get_no_jobs_heading() == "No Jobs Found", "Jobs not found heading does not match"
    assert jobs_page.get_no_jobs_description() == "We could not find any jobs. Try other filters.", "Jobs not found description does not match"
