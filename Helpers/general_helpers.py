from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time


class Helper():

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def go_to_page(self, url):
        self.driver.get(url)
        self.test_logger.info(f"{url} is opened.")

    def find_elem_ui(self, loc, sec=60):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_element_located(loc))
            return elem
        except Exception as e:
            self.test_logger.error("Element is not vissible.")
            self.test_logger.error(e)

    def find_elem_dom(self, loc, sec=60):
        elem = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        return elem

    def find_and_click(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except StaleElementReferenceException:
            # Retry once if stale
            time.sleep(1)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def find_and_send_keys(self, loc, inp_text, sec=60):
        elem = self.find_elem_ui(loc, sec)
        elem.send_keys(inp_text)

    def wait_until_clickable(self, locator, timeout=10):
    
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return element
    
    def hover_element(self, loc):
        actions = ActionChains(self.driver)
        hover = actions.move_to_element(self.find_elem_ui(loc)).pause(0.5)
        hover.perform()

    def wait_and_get_elements(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)
    
    #make locator dynamic
    def make_locator(self, *args):
        return args[0][0], args[0][1] % args[1:]
    

            
        
   