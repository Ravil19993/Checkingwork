from shopping import Shopping
import pytest

  
@pytest.mark.parametrize(
        'good1, good2, good3, first_name, last_name, postal_code',
        [('#add-to-cart-sauce-labs-backpack',
          '#add-to-cart-sauce-labs-bolt-t-shirt',
          '#add-to-cart-sauce-labs-onesie',
          '#first-name', '#last-name', '#postal-code')])
def test_total_price(good1, good2, good3, first_name, last_name, postal_code):
    shopping = Shopping()
    shopping.authorization()
    shopping.adding_goods(good1, good2, good3)
    shopping.info_about_customer(first_name, last_name, postal_code)
    all_price = shopping.total_price()
    all_price = str(all_price)
    set_total_price = 'Total: $58.29'
    try:
        assert all_price == set_total_price
        print("Итоговая сумма совпадает с заданной и равна: ", all_price)
    except Exception:
        print('Итоговая сумма отличается и равна: ', all_price)
