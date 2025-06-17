from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper

class ProductPage(Helper):
    add_to_bag_button = (By.ID, "add-to-cart-button") 
    view_bag_button = (By.XPATH, "//form[contains(@action, 'checkout')]//a[contains(., 'View Bag')]")      
    price_label = (By.XPATH, '//span[@aria-hidden="true" and span[@itemprop="priceCurrency"]]')  
    products = (By.XPATH, '//*[@id="products"]/article/a')

    def select_product(self, index):
        products = self.find_all(self.products)  
        products[index].click()

    def get_product_price(self):
        price_text = self.find(self.price_label).text
        print(price_text)
        return float(price_text.replace("$", "").strip())

    def add_to_bag(self):
        self.find_and_click(self.add_to_bag_button)

    def view_bag(self):
        self.find_and_click(self.view_bag_button)