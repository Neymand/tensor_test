import time
import requests
from selenium.webdriver.common.by import By
from base_page import BasePage
import os
import re



class DownPage(BasePage):

    DOWNLOAD_LOCAL_VERSION = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/ul/li[10]/a')
    DOWNLOAD_FILE_LINK = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')

    # def __init__(self, driver, download_dir):
    #     super().__init__(driver)
    #     self.download_dir = download_dir

    def trans_down_page(self):
        self.click_element(self.DOWNLOAD_LOCAL_VERSION)

    def download_file(self, download_dir):
        element = self.find_element(self.DOWNLOAD_FILE_LINK)
        file_url = element.get_attribute("href")
        response = requests.get(file_url)
        response.raise_for_status()

        # Создаем папку если не существует
        if download_dir:
            os.makedirs(download_dir, exist_ok=True)
            file_path = os.path.join(download_dir, 'saby-setup-web.exe')
        else:
            file_path = 'saby-setup-web.exe'

        with open(file_path, 'wb') as file:
            file.write(response.content)

    def get_expected_file_size(self):
        """Получает ожидаемый размер файла из текста ссылки"""
        element = self.find_element(self.DOWNLOAD_FILE_LINK)
        text = element.text
        return extract_file_size_from_text(text)

    def verify_file_size(self, file_path, tolerance=0.05):
        """
        Сравнивает фактический размер файла с указанным на странице
        tolerance - допустимое отклонение (5% по умолчанию)
        """
        expected_size = self.get_expected_file_size()
        actual_size = os.path.getsize(file_path)

        if expected_size is None:
            raise ValueError("Не удалось определить ожидаемый размер файла")

        # Проверяем соответствие с учетом допустимой погрешности
        size_diff = abs(actual_size - expected_size)
        allowed_diff = expected_size * tolerance

        return {
            'expected': expected_size,
            'actual': actual_size,
            'is_match': size_diff <= allowed_diff,
            'difference': actual_size - expected_size,
            'difference_percent': (size_diff / expected_size) * 100
        }

def extract_file_size_from_text(text):
    """
    Извлекает размер файла из текста вида "Скачать (Exe 10.40 МБ)"
    Возвращает размер в байтах
    """
    # Ищем число с плавающей точкой и единицы измерения
    match = re.search(r'(\d+\.?\d*)\s*(КБ|МБ|ГБ|Б)', text)
    if not match:
        return None

    size = float(match.group(1))
    unit = match.group(2)

    # Конвертируем в байты
    units = {
        'Б': 1,
        'КБ': 1024,
        'МБ': 1024 ** 2,
        'ГБ': 1024 ** 3
    }

    return size * units[unit]

