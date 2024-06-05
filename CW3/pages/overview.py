from selenium.webdriver.common.by import By


class Overview:
    def __init__(self, browser):
        self._driver = browser

    def total_price(self):
        a = self._driver.find_element(
            By.CSS_SELECTOR, '[class="summary_total_label"]').text

        return a
