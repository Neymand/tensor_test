import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех страниц
    """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://saby.ru"

    def go_to(self):
        self.driver.get(self.base_url)

    def verify_region(self, locator, expected_region, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_region))

    def find_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        element.click()
        time.sleep(5)

    def get_current_url(self):
        """Возвращает текущий URL страницы"""
        return self.driver.current_url

