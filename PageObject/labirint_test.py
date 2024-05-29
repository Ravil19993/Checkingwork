from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    #Перейти на сайт лабиринта
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    #найти все книги по слову питон
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("python")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "section.search-tab"))
    )
    #Добавить все книги в корзину и посчитать сколько
    buy_bottons = browser.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for btn in buy_bottons:
        btn.click()
        counter += 1
    #Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")
    #Проверить, что счетчик товаров должен быть равен числу нажатий
    a = browser.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']")
    txt = a.find_element(By.CSS_SELECTOR, "b").text
    txt = int(txt)
    assert counter == txt
    browser.quit()
