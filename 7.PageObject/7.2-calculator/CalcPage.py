from selenium.webdriver.common.by import By
from time import sleep


class Calculator:
    def __init__(self, browser):
        self._driver = browser
        self._driver.maximize_window()
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def counting(self, num_1, action, num_2, set_time):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(
            By.CSS_SELECTOR, "#delay").send_keys(set_time)
        self._driver.find_element(By.XPATH, num_1).click()
        self._driver.find_element(By.XPATH, action).click()
        self._driver.find_element(By.XPATH, num_2).click()
        self._driver.find_element(
            By.XPATH, "//*[contains(text(),'=')]").click()
        sleep(int(set_time))
        res = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return res
