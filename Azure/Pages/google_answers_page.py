from Utils.browser_utils import BrowserUtils
from Utils.file_utils import write_to_file
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import logging
from Utils.logger_utils import logger
logger()


class GoogleAnswersPage(BrowserUtils):
    google_answer = (By.XPATH, "//div[@data-attrid='wa:/description']/span | //div[@data-attrid='description']/span")

    def __init__(self, driver):
        super().__init__(driver)

    def write_search_answer(self):
        logging.info("Capturing Google answer from search results...")
        try:
            google_answer_element = self.wait_for_element(self.google_answer)
            write_to_file("Searched: " + google_answer_element.text)
            logging.info(f"Answer found and logged: {google_answer_element.text}")
        except TimeoutException:
            logging.warning("Timeout: Couldn't find the featured snippet or description.")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")(f"Unexpected error occurred: {e}")