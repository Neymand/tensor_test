# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
# TENSOR_BANNER = (By.XPATH, "//img[contains(@alt,'Разработчик системы Saby — компания «Тензор»')]")
#
# driver.get("https://saby.ru/contacts")
#
# # Явное ожидание элемента
#
# banner_element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(TENSOR_BANNER)
# )
# banner_element.click()
#
#
# time.sleep(5)

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://saby.ru"

    def go_to(self):
        self.driver.get(self.base_url)

    def verify_region(self, locator, expected_region, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_region))

    def find_element(self, locator, timeout=15):
        print(WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)))
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=15):
        element = self.find_element(locator, timeout)
        element.click()
        time.sleep(2)

    def get_current_url(self):
        """Возвращает текущий URL страницы"""
        return self.driver.current_url

