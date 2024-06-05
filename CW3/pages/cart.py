from selenium.webdriver.common.by import By


class CheckCart:
    def __init__(self, browser):
        self._driver = browser

    def checking_cart(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '#checkout').click()
