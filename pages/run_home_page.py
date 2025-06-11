import time

# run_home_page.py

from selenium import webdriver
from pages.home_page import HomePage
from pages.tensor_page import TensorPage

def test_home_page():
    driver = webdriver.Chrome()  # Убедитесь, что WebDriver доступен в PATH
    try:
        home_page = HomePage(driver)
        home_page.go_to()  # Переход на главную страницу saby.ru
        home_page.go_to_contacts()  # Выполняем переход на страницу контактов

        tensor_page = TensorPage(driver)
        tensor_page.is_people_power_block_present()

        tensor_page.get_work_section_images()

    finally:
        driver.quit()

if __name__ == "__main__":
    test_home_page()
