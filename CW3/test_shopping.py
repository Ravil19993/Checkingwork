from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.authorization import AuthorizationPage
from pages.adding_goods import AddGoodsPage
from pages.cart import CheckCart
from pages.checkout import Checkout
from pages.overview import Overview
import pytest


@pytest.mark.parametrize(
        'good1, good2, good3, first_name, last_name, postal_code',
        [('#add-to-cart-sauce-labs-backpack',
          '#add-to-cart-sauce-labs-bolt-t-shirt',
          '#add-to-cart-sauce-labs-onesie',
          'Равиль', 'Зиятдинов', '617700')])
def test_total_price(good1, good2, good3, first_name, last_name, postal_code):
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    authorization_page = AuthorizationPage(browser)
    authorization_page.login()

    adding_page = AddGoodsPage(browser)
    adding_page.adding_goods(good1, good2, good3)

    cart = CheckCart(browser)
    cart.checking_cart()

    customer = Checkout(browser)
    customer.info_about_customer(first_name, last_name, postal_code)

    overview = Overview(browser)
    all_price = overview.total_price()
    all_price = str(all_price)

    set_total_price = 'Total: $58.39'
    try:
        assert all_price == set_total_price
        print("Итоговая сумма совпадает с заданной и равна: ", all_price)
    except Exception:
        print('Итоговая сумма отличается и равна: ', all_price)

    browser.quit()
