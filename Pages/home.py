from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import Teastdata.config as config


class Searche(Helper):

    search_field = (By.ID, "searchAll")
    search_loop = (By.XPATH, "//*[@id='searchForm']/button")
    color = (By.XPATH, '//*[@data-test-id-facet-head-name = "Color"]')
    brand = (By.XPATH, "//*[@data-test-id-facet-head-name = 'Brand']")
    price = (By.XPATH, '//*[@data-test-id-facet-head-name = "Price"]')
    raen_optics = (By.XPATH, "//a[@class='Ss-z']/span[text()='RAEN Optics']")
    price_dol200 = (By.XPATH, "//span[text()='$200.00 and Under']") 
    orange = (By.XPATH, "//span[text()='Orange']")
    result_text = (By.CSS_SELECTOR, "span.ft-z")
    visible_product_count = (By.XPATH, '//*[@id="products"]/article')
    products_elements = (By.CSS_SELECTOR, "#products > article > a")

    def search_item(self):
        self.find_and_send_keys(self.search_field, config.text_data)
        self.find_and_click(self.search_loop)
        self.find_and_click(self.brand)
        self.hover_element(self.raen_optics)
        self.find_and_click(self.raen_optics)
        self.find_and_click(self.price)
        self.find_and_click(self.price_dol200)
        self.find_and_click(self.color)
        self.find_and_click(self.orange)

    def get_visible_product_count(self):
        return len(self.wait_and_get_elements(self.visible_product_count))
           
    def get_reported_result_count(self):
        text = self.driver.find_element(*self.result_text).text
        return int(text.split()[0])
    
    def get_all_product_brands(self):
        brand_elements = self.driver.find_elements(*self.products_elements) 
        brand = [el.text.split(" -")[0] for el in brand_elements]
        return [el.lower() for el in brand] 

    def get_all_product_prices(self):
        price_elements = self.driver.find_elements(*self.products_elements)
        print(f"price = : {price_elements}")  
        prices = []
        for el in price_elements:
            price_text = el.text.split("$")[1]  
            price_text = price_text.split(". MSRP")[0]
            try:
                price = float(price_text)       
                prices.append(price)
            except ValueError:
                continue
        return prices
    
        
