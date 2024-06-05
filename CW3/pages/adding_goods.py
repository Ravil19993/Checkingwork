from selenium.webdriver.common.by import By


class AddGoodsPage:
    def __init__(self, browser):
        self._driver = browser

    def adding_goods(self, good1, good2, good3):
        self._driver.find_element(By.CSS_SELECTOR, good1).click()
        self._driver.find_element(By.CSS_SELECTOR, good2).click()
        self._driver.find_element(By.CSS_SELECTOR, good3).click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'a.shopping_cart_link').click()
