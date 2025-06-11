from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    CONTACT = (By.LINK_TEXT, "Контакты")
    REGION_DISPLAY = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')


    def get_region_locator(self, region_name):
        return (By.XPATH, f"//span[contains(@title,'{region_name}')]//span[1]")

    def open_contacts(self):
        # Метод для открытия раздела "Контакты" на saby.ru
        self.click_element(self.CONTACT)


    def verify_current_region(self, expected_region):
        self.verify_region(self.REGION_DISPLAY, expected_region)

    def change_region(self, region_name):
        region_locator = self.get_region_locator(region_name)
        self.click_element(self.REGION_DISPLAY)
        self.click_element(region_locator)

    def current_url(self):
        return self.get_current_url()

    def verify_region_and_partners(self, expected_region):
        self.verify_current_region(expected_region)


    #     # Здесь вы можете добавить проверку списка партнеров
        #assert self.driver.title.contains(expected_region), "Title doesn't contain expected region"