from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )


cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def go_to_site():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def search_books(term):
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "section.search-tab"))
    )


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
    go_to_site()
    search_books('python')
    added = add_books()
    go_to_cart()
    amount_in_cart = count_added_books()
    close_browser()
    assert added == amount_in_cart
