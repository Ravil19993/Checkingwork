from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


class Calculator:
    def counting(self, num_1, action, num_2, set_time):
        driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(set_time)
        driver.find_element(By.XPATH, num_1).click()
        driver.find_element(By.XPATH, action).click()
        driver.find_element(By.XPATH, num_2).click()
        driver.find_element(By.XPATH, "//*[contains(text(),'=')]").click()
        sleep(int(set_time))
        res = driver.find_element(By.CSS_SELECTOR, "div.screen").text
        driver.quit()
        return res
