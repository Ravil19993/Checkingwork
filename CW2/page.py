from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Color:
    def __init__(self, browser):
        self._driver = browser

    def get_background_color(self, zip_code, first_name, last_name, address,
                             e_mail, phone, city, country, job_position,
                             company):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").\
            send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").\
            send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").\
            send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").\
            send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").\
            send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").\
            send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").\
            send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").\
            send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").\
            send_keys("SkyPro")

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3')
                )).click()

        zip_code = self._driver.find_element(By.CSS_SELECTOR, zip_code).\
            value_of_css_property('background-color')
        first_name = self._driver.find_element(By.CSS_SELECTOR, first_name).\
            value_of_css_property('background-color')
        last_name = self._driver.find_element(By.CSS_SELECTOR, last_name).\
            value_of_css_property('background-color')
        address = self._driver.find_element(By.CSS_SELECTOR, address).\
            value_of_css_property('background-color')
        e_mail = self._driver.find_element(By.CSS_SELECTOR, e_mail).\
            value_of_css_property('background-color')
        phone = self._driver.find_element(By.CSS_SELECTOR, phone).\
            value_of_css_property('background-color')
        city = self._driver.find_element(By.CSS_SELECTOR, city).\
            value_of_css_property('background-color')
        country = self._driver.find_element(By.CSS_SELECTOR, country).\
            value_of_css_property('background-color')
        job_position = self._driver.find_element(
            By.CSS_SELECTOR, job_position).value_of_css_property(
                'background-color')
        company = self._driver.find_element(By.CSS_SELECTOR, company).\
            value_of_css_property('background-color')
        return zip_code, first_name, last_name, address, e_mail, phone, city, \
            country, job_position, company
