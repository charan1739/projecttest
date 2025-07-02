import pytest
import time
from selenium import webdriver
from login_page import LoginPage
from header_section import HeaderSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def header(driver):
    login_page = LoginPage(driver)
    login_page.login("rahul", "rahul@2021")
    time.sleep(2)
    yield HeaderSection(driver)

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qajobbyapp.ccbp.tech/login")
    yield driver
    driver.quit()


def test_app_logo_displayed(header):
    WebDriverWait(header.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.website-logo")))
    assert header.is_logo_displayed(), "App logo is not displayed"


def test_nav_jobs_link(header):
    header.click_nav_jobs()
    time.sleep(2)
    assert header.driver.current_url == "https://qajobbyapp.ccbp.tech/jobs", "URLs do not match"


def test_logo_link_navigation(header):
    header.click_nav_jobs()
    time.sleep(1)
    header.click_logo_link()
    time.sleep(1)
    assert header.driver.current_url == "https://qajobbyapp.ccbp.tech/", "URLs do not match"


def test_nav_home_link(header):
    header.click_nav_jobs()
    time.sleep(1)
    header.click_nav_home()
    time.sleep(1)
    assert header.driver.current_url == "https://qajobbyapp.ccbp.tech/", "URLs do not match"


def test_logout_button(header):
    header.click_logout()
    time.sleep(2)
    assert header.driver.current_url == "https://qajobbyapp.ccbp.tech/login", "URLs do not match"
