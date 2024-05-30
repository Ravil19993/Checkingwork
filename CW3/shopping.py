from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')


class Shopping:
    def authorization(self):
        driver.find_element(
            By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        driver.find_element(
            By.CSS_SELECTOR, '.submit-button.btn_action').click()

    def adding_goods(self, good1, good2, good3):
        driver.find_element(By.CSS_SELECTOR, good1).click()
        driver.find_element(By.CSS_SELECTOR, good2).click()
        driver.find_element(By.CSS_SELECTOR, good3).click()
        driver.find_element(
            By.CSS_SELECTOR, 'a.shopping_cart_link').click()
        driver.find_element(
            By.CSS_SELECTOR, '#checkout').click()

    def info_about_customer(self, first_name, last_name, postal_code):
        driver.find_element(
            By.CSS_SELECTOR, first_name).send_keys('Равиль')
        driver.find_element(
            By.CSS_SELECTOR, last_name).send_keys('Зиятдинов')
        driver.find_element(
            By.CSS_SELECTOR, postal_code).send_keys('617700')
        driver.find_element(
            By.CSS_SELECTOR, '#continue').click()

    def total_price(self):
        a = driver.find_element(
            By.CSS_SELECTOR, '[class="summary_total_label"]').text
        driver.quit()
        return a
