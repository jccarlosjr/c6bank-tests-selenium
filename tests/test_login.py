import pytest
from pages.login_page import LoginPage
from drivers.driver_setup import init_chromedriver
from config.config import CHROMEDRIVER_PATH, USER, PASSWORD


@pytest.fixture
def driver():
    driver = init_chromedriver(CHROMEDRIVER_PATH)
    yield driver
    driver.quit()

def test_login_success(driver):
    page = LoginPage(driver)
    page.access("https://c6.c6consig.com.br/WebAutorizador/")
    page.login(USER, PASSWORD)
    page.is_logged_in()


def test_login_failure(driver):
    page = LoginPage(driver)
    page.access("https://c6.c6consig.com.br/WebAutorizador/")
    with pytest.raises(Exception):
        page.login("invalid_user", "invalid_password")


def test_login_page_structure(driver):
    page = LoginPage(driver)
    page.access("https://c6.c6consig.com.br/WebAutorizador/")
    
    assert driver.find_element(*page.user_input), "User input field is missing."
    assert driver.find_element(*page.pass_input), "Password input field is missing."
    assert driver.find_element(*page.login_btn), "Login button is missing."
    
    # Check if the login button is enabled
    login_button = driver.find_element(*page.login_btn)
    assert login_button.is_enabled(), "Login button should be enabled." 