import pytest
from selenium import webdriver
from login_page import LoginPage
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qajobbyapp.ccbp.tech/login")
    yield driver
    driver.quit()

def test_login_page_ui(driver):
    login_page = LoginPage(driver)

    assert login_page.is_logo_displayed(), "App logo is not displayed"
    assert login_page.get_label_text(0) == "USERNAME", "Username label text does not match"
    assert login_page.get_label_text(1) == "PASSWORD", "Password label text does not match"

def test_empty_inputs(driver):
    login_page = LoginPage(driver)

    login_page.click_login()
    assert login_page.get_error_message() == "*Username or password is invalid", "Error text with empty input fields does not match"

def test_empty_username(driver):
    login_page = LoginPage(driver)

    login_page.enter_password("rahul@2021")
    login_page.click_login()
    assert login_page.get_error_message() == "*Username or password is invalid", "Error text with empty input field do not match"

def test_empty_password(driver):
    login_page = LoginPage(driver)

    login_page.enter_username("rahul")
    login_page.click_login()
    assert login_page.get_error_message() == "*Username or password is invalid", "Error text with empty input field do not match"

def test_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("rahul", "rahul")
    assert login_page.get_error_message() == "*username and password didn't match", "Error text with invalid password do not match"

def test_successful_login(driver):
    login_page = LoginPage(driver)

    login_page.login("rahul", "rahul@2021")
    time.sleep(2)
    assert driver.current_url == "https://qajobbyapp.ccbp.tech/", "URLs do not match"