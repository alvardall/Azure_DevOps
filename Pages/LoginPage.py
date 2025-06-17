from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import config


class LoginPage(Helper):
    account_login_button = (By.XPATH, "//a[@data-header-account-toggle='true']")
    email_field = (By.ID, "ap_email")
    password_field = (By.ID, "ap_password")
    sign_in_button = (By.ID, "signInSubmit")

    def login(self):
        self.find_and_click(self.account_login_button)
        self.find_and_send_keys(self.email_field, config.login_email)
        self.find_and_send_keys(self.password_field, config.login_password)
        self.find_and_click(self.sign_in_button)
        self.test_logger.info("User logged in.")