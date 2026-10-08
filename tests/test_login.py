import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from base.config import BASE_URL, VALID_USERNAME, INVALID_PASSWORD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

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

def test_TC20_login_button_clickable(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    login_button = login_page.wait.until(
        EC.element_to_be_clickable(login_page.LOGIN_BUTTON)
    )

    assert login_button.is_displayed()
    assert login_button.is_enabled()

def test_TC21_submit_login_with_enter(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    login_page.enter_username("invalid_user_12345")
    password_input = driver.find_element(*login_page.PASSWORD_INPUT)
    password_input.send_keys("wrong_password_12345")
    password_input.send_keys(Keys.ENTER)

    error_message = login_page.get_error_message()

    assert error_message == "Tài khoản hoặc mật khẩu không đúng."

def test_TC22_multiple_login_clicks(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    for _ in range(3):
        login_page.enter_username("invalid_user_12345")
        login_page.enter_password("wrong_password_12345")
        login_page.click_login()

        login_page.wait.until(
            EC.presence_of_element_located(login_page.LOGIN_BUTTON)
        )

def test_TC23_reload_login_page(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    driver.refresh()

    username_input = login_page.wait.until(
        EC.visibility_of_element_located(login_page.USERNAME_INPUT)
    )

    password_input = login_page.wait.until(
        EC.visibility_of_element_located(login_page.PASSWORD_INPUT)
    )

    assert username_input.is_displayed()
    assert password_input.is_displayed()

def test_TC24_direct_login_url(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    assert driver.current_url.startswith(BASE_URL)

def test_TC25_username_placeholder(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    assert login_page.get_username_placeholder() == "Tên đăng nhập"

def test_TC26_password_placeholder(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    assert login_page.get_password_placeholder() == "Mật khẩu"

def test_TC27_login_button(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    button = driver.find_element(*login_page.LOGIN_BUTTON)

    assert button.is_displayed()
    assert button.is_enabled()
    assert login_page.get_login_button_text() == "Đăng nhập"

def test_TC28_remember_me_state_change(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    checkbox = driver.find_element(*login_page.REMEMBER_ME)

    assert checkbox.is_selected() is False

    remember_label = login_page.wait.until(
        EC.element_to_be_clickable(login_page.REMEMBER_ME_LABEL)
    )

    remember_label.click()

    checkbox = driver.find_element(*login_page.REMEMBER_ME)

    assert checkbox.is_selected() is True

def test_TC29_remember_me_default_state(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    checkbox = driver.find_element(*login_page.REMEMBER_ME)

    assert checkbox.is_selected() is False

def test_TC31_login_with_utc_email(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    email_login_link = login_page.wait.until(
        EC.element_to_be_clickable(login_page.EMAIL_LOGIN_LINK)
    )

    email_login_link.click()

    login_page.wait.until(
        lambda d: "accounts.google.com" in d.current_url
    )

    assert "accounts.google.com" in driver.current_url

def test_TC32_forgot_password_navigation(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)

    forgot_password_link = login_page.wait.until(
        EC.element_to_be_clickable(login_page.FORGOT_PASSWORD_LINK)
    )

    forgot_password_link.click()

    login_page.wait.until(
        lambda d: d.current_url.endswith("/Login/GetPass")
    )

    assert driver.current_url.endswith("/Login/GetPass")