from selenium.webdriver.common.by import By
from faker import Faker
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

fake = Faker('ru_RU')


class Color:
    def __init__(self, browser):
        self._driver = browser
        self._driver.maximize_window()

    def get_background_color(self, zip_code, first_name, last_name, address,
                             e_mail, phone, city, country, job_position,
                             company):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").\
            send_keys(fake.first_name_male())
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").\
            send_keys(fake.last_name_male())
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").\
            send_keys(fake.street_address())
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").\
            send_keys(fake.ascii_free_email())
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").\
            send_keys(fake.phone_number())
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").\
            send_keys(fake.city())
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").\
            send_keys(fake.country())
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").\
            send_keys(fake.job())
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").\
            send_keys(fake.company())
        sleep(4)

        self._driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")
        element = self._driver.find_element_by_id("my-id")
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()
        self._driver.find_element(
            By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

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
