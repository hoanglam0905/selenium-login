import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from config import BASE_URL, VALID_USERNAME, INVALID_PASSWORD


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