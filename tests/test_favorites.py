import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from Pages.LoginPage import LoginPage
from Pages.accessories import AccessoriesPage
from Pages.FavoritesPage import FavoritesPage
import Testdata.data as data


def test_favorites_feature(test_driver, test_logger):
    login_page = LoginPage(test_driver, test_logger)
    accessories_page = AccessoriesPage(test_driver, test_logger)
    favorites_page = FavoritesPage(test_driver, test_logger)

    login_page.go_to_page(config.url)
    login_page.login()
    
    accessories_page.go_to_accessories()
    accessories_page.select_watches()
    accessories_page.clear_favorites()
    accessories_page.add_favorites(count=len(data.favorites_to_add))

    favorites_page.go_to_favorites()
    favorite_items = favorites_page.get_favorite_count()
    test_logger.info(f"Favorites found: {favorite_items}")

    assert favorite_items == len(data.favorites_to_add), f"Favorite items count is not maches"

    
