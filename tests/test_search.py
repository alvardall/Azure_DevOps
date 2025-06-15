import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Teastdata.config as config
from Pages.home import Searche

def test_valid_data(test_driver, test_logger):

    searche_obj = Searche(test_driver, test_logger)
    searche_obj.go_to_page(config.url)
    searche_obj.search_item()
    test_logger.info("Performed search")

    result_count = searche_obj.get_reported_result_count() 
    test_logger.info(f"RESULT COUNT: {result_count}")

    visible_count = searche_obj.get_visible_product_count()

    assert visible_count == result_count, f"Visible items ({visible_count}) don't match reported count ({result_count})"
    test_logger.info("Visible count matches reported count")

    brands = searche_obj.get_all_product_brands()
    
    assert config.brand.lower() in brands, f"Unexpected brand: {brands}"
    test_logger.info(f" Brand '{brands}' matches expected '{config.brand}'")

    prices = searche_obj.get_all_product_prices()
    
    for p in prices:
        assert p <= 200.0, f"Price out of range: {p}"
    test_logger.info(f" Price within range: {p}")

    test_logger.info(f"All test is finished")







    