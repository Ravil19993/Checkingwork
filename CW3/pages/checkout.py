from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, browser):
        self._driver = browser

    def info_about_customer(self, first_name, last_name, postal_code):
        self._driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self._driver.find_element(
            By.CSS_SELECTOR, '#continue').click()
