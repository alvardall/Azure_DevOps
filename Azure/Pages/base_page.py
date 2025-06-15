from selenium.webdriver.common.action_chains import ActionChains
from Utils.browser_utils import BrowserUtils
from Utils.file_utils import write_to_file
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
import logging
from Utils.logger_utils import logger
logger()


class BasePage(BrowserUtils):
    alert_button = (By.CSS_SELECTOR, "#alertbtn")
    hide_show_field = (By.ID, "displayed-text")
    hide_button = (By.ID, "hide-textbox")
    mouse_hover_btn = (By.ID, "mousehover")
    top_option = (By.LINK_TEXT, "Top")
    footer_text = (By.CSS_SELECTOR, "p.small.dynamic-text.jqCopyRight")

    def __init__(self, driver):
        super().__init__(driver)

    def handle_alert(self):
        try:
            logging.info("Handling alert...")
            self.wait_until_clickable(self.alert_button).click()
            alert_popupWindow = self.driver.switch_to.alert
            write_to_file(f"Alert Text:  {alert_popupWindow.text}")
            alert_popupWindow.accept()
            logging.info("Alert accepted.")
        except (NoSuchElementException, TimeoutException, UnexpectedAlertPresentException) as e:
            logging.error(f"Error while handling alert: {e}")

    def hide_and_log(self):
        try:
            logging.info("Clicking hide button and logging visibility...")
            self.wait_until_clickable(self.hide_button).click()
            textbox = self.wait_for_element(self.hide_show_field)
            style_value = textbox.get_attribute("style")
            write_to_file(f'Textbox visibility control: style="{style_value}"')
            logging.info(f"Textbox style: {style_value}")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error while hiding and logging textbox: {e}")

    def mouse_hover_click_top(self):
        try:
            logging.info("Performing mouse hover and clicking 'Top'...")
            hover_btn = self.wait_for_element(self.mouse_hover_btn)
            actions = ActionChains(self.driver)
            actions.move_to_element(hover_btn).perform()
            self.wait_until_clickable(self.top_option).click()
            logging.info("Clicked on 'Top'.")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error during mouse hover and click: {e}")

    def write_footer_text(self):
        try:
            logging.info("Scrolling to footer and logging text...")
            footer_text_element = self.wait_for_element(self.footer_text)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_text_element)
            write_to_file(f"Footer text:  {footer_text_element.text}")
            logging.info(f"Footer text: {footer_text_element.text}")
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Error while writing footer text: {e}")