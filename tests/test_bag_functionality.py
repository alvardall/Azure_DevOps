import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import config
from Pages.LoginPage import LoginPage
from Pages.searchPage import Searche
from Pages.productPage import ProductPage
from Pages.bagPage import BagPage


def test_add_to_bag_functionality(test_driver, test_logger):
    login_page = LoginPage(test_driver, test_logger)
    search_page = Searche(test_driver, test_logger)
    product_page = ProductPage(test_driver, test_logger)
    bag_page = BagPage(test_driver, test_logger)

    login_page.go_to_page(config.url)
    login_page.login()

    search_page.search_item()

    product_page.select_product(index=0)
    first_price = product_page.get_product_price()
    product_page.add_to_bag()
    test_logger.info("Added 1st sunglasses to the bag.")

    product_page.view_bag()
    
    bag_count = bag_page.get_bag_count()
    bag_price = bag_page.get_bag_price()
    assert bag_count == 1, "Bag count should be 1"
    assert bag_price == first_price, "Bag price should match 1st item"

    search_page.search_item()
    product_page.select_product(index=1)
    second_price = product_page.get_product_price()
    product_page.add_to_bag()
    test_logger.info("Added 2nd sunglasses to the bag.")
    product_page.view_bag()

    final_count = bag_page.get_bag_count()
    final_price = bag_page.get_bag_price()
    expected_total = first_price + second_price

    assert final_count == 2, "Bag count should be 2"
    assert abs(final_price - expected_total) < 0.01, "Subtotal price should match sum of two products"

    test_logger.info(" Add to Bag functionality test passed.")