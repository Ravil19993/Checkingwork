import pytest
from calc import Calculator
    
    
@pytest.mark.parametrize('num_1, action, num_2, set_result, set_time', [('//*[contains(text(),"7")]', '//*[contains(text(),"+")]', '//*[contains(text(),"8")]', '15', '45')])
def test_calc(num_1, action, num_2, set_result, set_time):
    
    calc = Calculator()
    res = calc.counting(num_1, action, num_2, set_time)
    print("Результат отобразился через ", set_time, "секунд")
    assert res == set_result