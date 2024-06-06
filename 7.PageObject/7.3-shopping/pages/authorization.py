from selenium.webdriver.common.by import By


class AuthorizationPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')

    def login(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self._driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(
            By.CSS_SELECTOR, '.submit-button.btn_action').click()
