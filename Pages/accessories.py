from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import time


class AccessoriesPage(Helper):
    department_menu = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/header/div[2]/ul/li[4]/a')
    category_watches = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/header/div[2]/ul/li[4]/div/div/div[1]/div[1]/ul/li[3]/a')
    product_favorite_button = (By.XPATH, '//*[@id="products"]/article//button') 
    remove_buttons = (By.XPATH, '//article//button[@aria-pressed="true"]') 

    def go_to_accessories(self):
        self.hover_element(self.department_menu)
        self.test_logger.info("Navigated to Accessories department.")

    def select_watches(self):
        self.find_and_click(self.category_watches)
        self.test_logger.info("Selected Watches category.")

    def clear_favorites(self):
        
        time.sleep(2)  # Wait for all items to load
        remove_btns = self.find_all(self.remove_buttons)
        for btn in remove_btns:
            btn.click()
            time.sleep(0.5)  # Prevent click conflict
        self.test_logger.info(f"Cleared {len(remove_btns)} favorite items.")

    def add_favorites(self, count):
        favorite_buttons = self.find_all(self.product_favorite_button)
        for i in range(min(count, len(favorite_buttons))):
            favorite_buttons[i].click()
            self.test_logger.info(f"Added watch {i+1} to favorites.")