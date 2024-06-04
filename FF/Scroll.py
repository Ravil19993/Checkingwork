#Научиться скроллить страницу до необходимого элемента

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(options=webdriver.FirefoxOptions())

driver.get('https://labirint.ru')
driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys('python')
driver.find_element(By.CSS_SELECTOR, 'button.b-header-b-search-e-btn').click()
sleep(2)

#Скролл до выбранного элемента
element = driver.find_element(By.CSS_SELECTOR, '[title="Python для детей"]')
driver.execute_script("arguments[0].scrollIntoView(true);", element)

sleep(2)
driver.quit()