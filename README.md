This framework is designed for UI automation testing of (https://www.6pm.com/) 
using Python, Selenium, PyTest, and Allure reports.

AGBU_Alvard_KarapetQristine_Varjuhi/
│
├── config.py # Configuration for URL and credentials
├── conftest.py # Fixtures for driver, logger, screenshot hook
├── pytest.ini # Pytest configuration
├── requirements.txt # Dependencies
│
├── Helpers/
│ └── general_helpers.py # Common WebDriver helper functions
│
├── Pages/ # Page Object Model classes
│ ├── loginPage.py
│ ├── searchPage.py
│ ├── productPage.py
│ ├── bagPage.py
│ └── ...
│
├── Testdata/
│ └── data.py # Test input data (text, price, brands)
│
└── tests/ # Test cases
├── test_bag_functionality.py
├── test_favorites.py
└── test_search.py



# 1. Clone the repo and navigate:

git https://github.com/alvardall/AGBU_Alvard_KarapetQristine_Varjuhi.git
cd AGBU_Alvard_KarapetQristine_Varjuhi

pip install -r requirements.txt

# 2. Create a virtual environment and activate it:
pip install -r requirements.txt

# 3 Run all tests
pytest

# 4 Run specific test file:

pytest tests/test_search.py

# 5 Run tests with Allure reporting:

pytest --alluredir=allure-results
allure serve allure-results

Features
Page Object Model (POM) Design Pattern
Logging per test with unique log files
Dynamic locator formatting
Robust element finding methods with waits
Test markers (smoke, regression)
Allure screenshots on failure

test_bag_functionality.py   Checks whether products are added to the cart-  Bag count, total price
test_favorites.py   Checks adding favorites-   Number of favorites
test_search.py  Checks search and filtering functionality   Visible vs reported count, brand, price range

Sample Credentials

Email:    allatest33@gmail.com
Password: test4554


Author
Developed by Alvard Telunts, Qristine Karapetyan, Varjuhi Muradyan (2025)
