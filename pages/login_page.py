from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    REMEMBER_ME = (By.ID, "persistent")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".submit_login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error")
    EMAIL_LOGIN_LINK = (
    By.CSS_SELECTOR,
    'a.button[href*="accounts.google.com/o/oauth2/auth"]'
)
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        button.click()

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text

    def get_password_input_type(self):
        element = self.wait.until(
        EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        return element.get_attribute("type")
    
