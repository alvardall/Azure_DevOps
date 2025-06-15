from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BrowserUtils:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def open_browser():
        try:
            driver = webdriver.Chrome()
            logging.info("Browser opened successfully.")
            return driver
        except Exception as e:
            logging.error(f"Failed to open browser: {e}")
            raise

    def wait_for_element(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logging.info(f"Element located: {locator}")
            return element
        except Exception as e:
            logging.error(f"Error locating element {locator}: {e}")
            raise

    def wait_until_clickable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            logging.info(f"Element is clickable: {locator}")
            return element
        except Exception as e:
            logging.error(f"Error waiting for element to be clickable {locator}: {e}")
            raise

    def wait_for_visible(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logging.info(f"Element is visible: {locator}")
            return element
        except Exception as e:
            logging.error(f"Error waiting for element to be visible {locator}: {e}")
            raise