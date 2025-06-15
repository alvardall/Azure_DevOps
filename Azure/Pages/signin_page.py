from Utils.browser_utils import BrowserUtils
from Utils.file_utils import write_to_file
import testData.data as data
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import logging
from Utils.logger_utils import logger
logger()


class SignInPage(BrowserUtils):
    signin_button = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')
    email_field = (By.ID, "email")
    password_field = (By.ID, "login-password")
    login_button = (By.ID, "login")
    error_message = (By.ID, "incorrectdetails")

    def __init__(self, driver):
        super().__init__(driver)

    def perform_login(self):
        try:
            time.sleep(3)
            logging.info("Attempting to log in...")
            self.wait_for_element(self.signin_button).click()
            self.wait_for_element(self.email_field).send_keys(data.inputEmail)
            self.wait_for_element(self.password_field).send_keys(data.inputPassword)
            self.wait_for_element(self.login_button).click()
            error_element = self.wait_for_visible(self.error_message)
            error = error_element.text
            write_to_file(f"Login Error:  {error}")
            logging.info(f"Login error message logged: {error}")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error during login attempt: {e}")