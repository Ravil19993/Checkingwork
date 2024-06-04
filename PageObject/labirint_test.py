from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.MainPage import MainPage




def add_books():
    buy_bottons = browser.find_elements(
        By.CSS_SELECTOR, "._btn.btn-tocart.buy-link"
        )
    counter = 0
    for btn in buy_bottons:
        btn.click()
        counter += 1
    return counter


def go_to_cart():
    browser.get("https://www.labirint.ru/cart/")


def count_added_books():
    amount_of_added_books = browser.find_element(
        By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(
            By.CSS_SELECTOR, "b").text
    return int(amount_of_added_books)


def close_browser():
    browser.quit()


def test_cart_counter():
    browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    