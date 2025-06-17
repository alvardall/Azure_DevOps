from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import re


class BagPage(Helper):
    item_count = (By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div/div/div/h3')
    subtotal_price = (By.XPATH, "//dt[contains(text(), 'Subtotal')]/following-sibling::dd")

    def get_bag_count(self):
        
        count_text = self.find(self.item_count).text
        count = int(re.search(r'\((\d+)', count_text).group(1))  
        return count

    def get_bag_price(self):
        price_text = self.find(self.subtotal_price).text
        return float(price_text.replace("$", "").strip())