from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import Testdata.data as data


class Searche(Helper):

    search_field = (By.ID, "searchAll")
    search_loop = (By.XPATH, "//*[@id='searchForm']/button")
    color_btn = (By.XPATH, '//*[@data-test-id-facet-head-name = "Color"]')
    brand = (By.XPATH, "//*[@data-test-id-facet-head-name = 'Brand']")
    price_btn = (By.XPATH, '//*[@data-test-id-facet-head-name = "Price"]')
    brand_name_btn = (By.XPATH, "//ul[@aria-labelledby='brandNameFacet']//span[text()='%s']")
    price_filter = (By.XPATH, "//ul[@aria-labelledby='priceFacet']//span[text()='%s']") 
    color_filter = (By.XPATH, "//ul[@aria-labelledby='colorFacet']//span[text()='%s']")
    result_text = (By.XPATH, "//span[contains(text(), 'items found')]")
    visible_product_count = (By.XPATH, '//*[@id="products"]/article')
    products_elements = (By.CSS_SELECTOR, "#products > article > a")
    

    def search_item(self):
        self.find_and_send_keys(self.search_field, data.text_data)
        self.find_and_click(self.search_loop)
        
    def filter_item(self):    
        self.find_and_click(self.brand)
        self.find_and_click(self.remake_locator(self.brand_name_btn, data.brand))
        self.hover_element(self.price_btn) 
        self.find_and_click(self.price_btn)
        self.find_and_click(self.remake_locator(self.price_filter, data.price_range)) 
        self.find_and_click(self.color_btn)
        self.find_and_click(self.remake_locator(self.color_filter, data.color))

    def get_visible_product_count(self):
        return len(self.wait_and_get_elements(self.visible_product_count))
           
    def get_reported_result_count(self):
        text = self.find(self.result_text).text
        return int(text.split()[0])
    
    def get_all_product_brands(self):
        brand_elements = self.find_all(self.products_elements) 
        brand = [el.text.split(" -")[0] for el in brand_elements]
        return [el.lower() for el in brand] 

    def get_all_product_prices(self):
        price_elements = self.find_all(self.products_elements) 
        prices = []
        for el in price_elements:
            price_text = el.text.split("$")[1]  
            price_text = price_text.split(". MSRP")[0]     
            price = float(price_text)       
            prices.append(price)    
        
        return prices
    
    

    
        
