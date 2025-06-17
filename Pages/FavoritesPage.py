from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper

class FavoritesPage(Helper):
    favorites_tab = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/header/div[1]/div[3]/div[3]/a')
    favorite_count = (By.CSS_SELECTOR, "p.NQ-z > span") 
    

    def go_to_favorites(self):
        self.find_and_click(self.favorites_tab)
        self.test_logger.info("Navigated to Favorites page.")

    def get_favorite_count(self):
        count_text = self.find(self.favorite_count).text 
        return int(count_text.split()[0])

    
    