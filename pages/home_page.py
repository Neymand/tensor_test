import time

from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    CONTACTS_LINK = (By.XPATH, "//div[@class='sbisru-Header-ContactsMenu js-ContactsMenu']")
    MORE_OFFICE = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]/span')
    TENSOR_BANNER = (By.XPATH, "//a[@class='sbisru-Contacts__logo-tensor mb-12']//img[@alt='Разработчик системы Saby — компания «Тензор»']")

    def go_to_contacts(self):

        self.click_element(self.CONTACTS_LINK)
        self.click_element(self.MORE_OFFICE)
        self.click_element(self.TENSOR_BANNER)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])



