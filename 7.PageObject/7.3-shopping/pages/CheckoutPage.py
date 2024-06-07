from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker("ru_RU")


class Checkout:
    def __init__(self, browser):
        self._driver = browser

    def info_about_customer(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(fake.first_name_male())
        self._driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(fake.last_name_male())
        self._driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(fake.postcode())
        self._driver.find_element(
            By.CSS_SELECTOR, '#continue').click()
