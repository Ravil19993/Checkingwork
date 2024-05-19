from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')
    
def authorization():
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '.submit-button.btn_action').click()
    
        
def adding_goods():
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click() 
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        
        
def info_about_customer():
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Равиль')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Зиятдинов')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('617700')
    driver.find_element(By.CSS_SELECTOR, '#continue').click()
        
            
def total_price():
    a = driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]').text
    return a


authorization()
adding_goods()
info_about_customer()
all_price = total_price()

all_price = str(all_price)
set_total_price = 'Total: $58.29'

try:
    assert all_price == set_total_price
    print('Итоговая сумма совпадает с заданной и равна: ', all_price)
except:
    print('Итоговая сумма отличается и равна: ', all_price)