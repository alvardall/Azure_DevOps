import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import Testdata.data as data
from Pages.searchPage import Searche


def test_valid_data(test_driver, test_logger):

    searche_obj = Searche(test_driver, test_logger)
    searche_obj.go_to_page(config.url)
    searche_obj.search_item()
    searche_obj.filter_item()
    test_logger.info("Performed search")

    result_count = searche_obj.get_reported_result_count() 
    test_logger.info(f"RESULT COUNT: {result_count}")

    visible_count = searche_obj.get_visible_product_count()

    assert visible_count == result_count, f"Visible items ({visible_count}) don't match reported count ({result_count})"
    test_logger.info("Visible count matches reported count")

    brands = searche_obj.get_all_product_brands()
    
    assert data.brand.lower() in brands, f"Unexpected brand: {brands}"
    test_logger.info(f" Brand '{brands}' matches expected '{data.brand}'")

    prices = searche_obj.get_all_product_prices()
    assert all([price <= 200.0 for price in prices]), f" Found price out of range: {prices}"
    test_logger.info(f" Price within range: {prices}")

    test_logger.info(f"All test is finished")







    