
from selenium.webdriver.common.by import By
from base_page import BasePage

class TensorPage(BasePage):
    PEOPLE_POWER_BLOCK = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
    MORE_DETAILS = (By.XPATH, "//a[@href='/about'][contains(text(),'Подробнее')]")
    WORKING_BLOCK = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')


    def is_people_power_block_present(self):
        self.find_element(self.PEOPLE_POWER_BLOCK) # Проверить, что есть блок "Сила в людях"


    def open_tenser_about(self):
        self.click_element(self.MORE_DETAILS)  # убедитесь, что открывается https://tensor.ru/about

    def get_work_section_images(self):
        container = self.find_element(self.WORKING_BLOCK)
        images = container.find_elements(By.TAG_NAME, 'img')


        # for img in images:
        #     width = img.get_attribute('width')
        #     height = img.get_attribute('height')
        #     src = img.get_attribute('src')
        #     alt = img.get_attribute('alt')
        #     print(f"Изображение: {alt}\n  URL: {src}\n  Размер: {width} x {height}\n")




