from page import Color
import pytest


@pytest.mark.parametrize('zip, first_name, last_name, address, e_mail, phone, \
                         city, country, job_position, company',
                         [('#zip-code', '#first-name', '#last-name',
                           '#address', '#e-mail', '#phone', '#city',
                           '#country', '#job-position', '#company')])
def test_background_color(zip, first_name, last_name, address, e_mail, phone,
                          city, country, job_position, company):
    all_color = Color()
    res = all_color.get_background_color(zip, first_name, last_name, address,
                                         e_mail, phone, city, country,
                                         job_position, company)
    assert res == ('rgba(248, 215, 218, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',
                   'rgba(209, 231, 221, 1)', 'rgba(209, 231, 221, 1)',)
