import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time

@pytest.fixture()
def home_page():
    driver = webdriver.Chrome()
    driver.get("https://qajobbyapp.ccbp.tech/login")
    login_page = LoginPage(driver)
    login_page.login("rahul", "rahul@2021")
    time.sleep(2)
    yield HomePage(driver)
    driver.quit()

def test_homepage_heading(home_page):
    assert home_page.get_heading_text() == "Find The Job That Fits Your Life", "Heading text does not match"
    assert home_page.get_description_text() == "Millions of people are searching for jobs, salary information, company reviews. Find the job that fits your abilities and potential.", "Description text does not match"

def test_find_jobs_button(home_page):
    home_page.click_find_jobs()
    time.sleep(2)
    assert home_page.driver.current_url == "https://qajobbyapp.ccbp.tech/jobs", "URLs do not match"
