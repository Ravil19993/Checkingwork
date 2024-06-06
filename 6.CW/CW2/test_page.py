from page import Color
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.parametrize('zip, first_name, last_name, address, e_mail, phone, \
                         city, country, job_position, company',
                         [('#zip-code', '#first-name', '#last-name',
                           '#address', '#e-mail', '#phone', '#city',
                           '#country', '#job-position', '#company')])
def test_background_color(zip, first_name, last_name, address, e_mail, phone,
                          city, country, job_position, company):
    browser = webdriver.Chrome(
      service=ChromeService(ChromeDriverManager().install()))
    all_color = Color(browser)
    res = all_color.get_background_color(zip, first_name, last_name, address,
                                         e_mail, phone, city, country,
                                         job_position, company)
    assert res == ('rgba(248, 215, 218, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',)
    browser.quit()
