import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from base.config import BASE_URL, VALID_USERNAME, INVALID_PASSWORD
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_TC1_username_empty(driver):
    login_page = LoginPage(driver)

    # Step 1: Mở trang đăng nhập
    login_page.open(BASE_URL)

    # Step 2: Để trống username

    # Step 3: Nhập password
    login_page.enter_password(INVALID_PASSWORD)

    # Step 4: Click Login
    login_page.click_login()

    # Expected Output
    actual_message = login_page.get_error_message()

    assert actual_message == "Bạn chưa nhập tên đăng nhập"

def test_TC2_password_empty(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.enter_username(VALID_USERNAME)
    login_page.click_login()

    actual_message = login_page.get_error_message()

    assert actual_message == "Bạn chưa nhập mật khẩu"

def test_TC3_username_password_empty(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.click_login()

    actual_message = login_page.get_error_message()

    assert actual_message == "Bạn chưa nhập tên đăng nhập"

def test_TC4_invalid_username_password(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.enter_username("invalid_user_12345")
    login_page.enter_password("wrong_password_12345")
    login_page.click_login()

    actual_message = login_page.get_error_message()

    assert actual_message == "Tài khoản hoặc mật khẩu không đúng."

def test_TC5_password_is_masked(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    password_input = driver.find_element(
        *login_page.PASSWORD_INPUT
    )

    assert password_input.get_attribute("type") == "password"

def test_TC6_submit_with_enter(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    username = driver.find_element(
        *login_page.USERNAME_INPUT
    )

    username.send_keys(Keys.ENTER)

    actual_message = login_page.get_error_message()

    assert actual_message == "Bạn chưa nhập tên đăng nhập"

def test_TC17_password_is_masked(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    assert login_page.get_password_input_type() == "password"

def test_TC18_enter_username(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    username = "test_user_123"
    login_page.enter_username(username)

    username_input = driver.find_element(*login_page.USERNAME_INPUT)

    assert username_input.get_attribute("value") == username

def test_TC19_enter_password(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    password = "test_password_123"
    login_page.enter_password(password)

    password_input = driver.find_element(*login_page.PASSWORD_INPUT)

    assert password_input.get_attribute("value") == password