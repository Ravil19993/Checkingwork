from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.AuthorizationPage import AuthorizationPage
from pages.AddingGoodsPage import AddGoodsPage
from pages.CartPage import CheckCart
from pages.CheckoutPage import Checkout
from pages.OverviewPage import Overview
import pytest


@pytest.mark.parametrize(
        'good1, good2, good3',
        [('#add-to-cart-sauce-labs-backpack',
          '#add-to-cart-sauce-labs-bolt-t-shirt',
          '#add-to-cart-sauce-labs-onesie')]
          )
def test_total_price(good1, good2, good3):
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    authorization_page = AuthorizationPage(browser)
    authorization_page.login()

    adding_page = AddGoodsPage(browser)
    adding_page.adding_goods(good1, good2, good3)

    cart = CheckCart(browser)
    cart.checking_cart()

    customer = Checkout(browser)
    customer.info_about_customer()

    overview = Overview(browser)
    all_price = overview.total_price()
    all_price = str(all_price)

    set_total_price = 'Total: $58.29'
    assert all_price == set_total_price
    print("Итоговая сумма равна: ", all_price)

    browser.quit()
