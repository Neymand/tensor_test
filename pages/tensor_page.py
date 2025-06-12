
from selenium.webdriver.common.by import By
from base_page import BasePage

class TensorPage(BasePage):
    PEOPLE_POWER_BLOCK = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
    MORE_DETAILS = (By.XPATH, "//a[@href='/about'][contains(text(),'Подробнее')]")
    WORKING_BLOCK = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')


    def is_people_power_block_present(self):
        """
        Проверить, что есть блок "Сила в людях
        """
        self.find_element(self.PEOPLE_POWER_BLOCK)


    def open_tenser_about(self):
        """
        открывается https://tensor.ru/about
        """
        self.click_element(self.MORE_DETAILS)

    def get_work_section_images(self):
        """
        Собиарет картинки со страницы
        :return:
        """
        container = self.find_element(self.WORKING_BLOCK)
        images = container.find_elements(By.TAG_NAME, 'img')







