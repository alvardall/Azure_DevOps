from Utils.browser_utils import BrowserUtils
import testData.data as data
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
from Utils.logger_utils import logger
logger()


class GoogleSearchPage(BrowserUtils):
    search = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def open_new_tab_and_search(self):
        try:
            logging.info("Opening new tab for Google search...")
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(data.newTab)
            logging.info(f"Navigated to: {data.newTab}")
            search_box = self.wait_for_element(self.search)
            search_box.send_keys(data.textForSearch)
            search_box.send_keys(Keys.ENTER)
            logging.info(f"Searched for: {data.textForSearch}")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error while searching in Google: {e}")
        except Exception as ex:
            logging.error(f"Unexpected error during Google search: {ex}")