import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.browser_utils import BrowserUtils
from Pages.base_page import BasePage
from Pages.signin_page import SignInPage
from Pages.google_search_page import GoogleSearchPage
from Pages.google_answers_page import GoogleAnswersPage
import testData.data as data
import Utils.file_utils as file_utils


if __name__ == "__main__":
    
    driver = BrowserUtils.open_browser()
    driver.get(data.home_url)

    base_page = BasePage(driver)
    base_page.handle_alert()
    base_page.hide_and_log()
    base_page.mouse_hover_click_top()
    base_page.write_footer_text()

    signin_page = SignInPage(driver)
    signin_page.perform_login()

    google_search_page = GoogleSearchPage(driver)
    google_search_page.open_new_tab_and_search()

    google_answers_page = GoogleAnswersPage(driver)
    google_answers_page.write_search_answer()

    driver.switch_to.window(driver.window_handles[0])
    driver.quit()

    file_utils.cleanup()
