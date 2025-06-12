import pytest
from pages.download_page import DownPage
from selenium.webdriver.chrome.options import Options
from tests.test_driver import driver
import os
import time

chrome_options = Options()
chrome_options.add_argument("--headless")



@pytest.mark.parametrize('driver', ['https://saby.ru'], indirect=True)
def test_download_file(driver):
    """Тест скачивания файла"""
    download_dir = os.path.join(os.getcwd(), "downloads")
    page = DownPage(driver)
    page.trans_down_page()
    page.download_file(download_dir)


    assert os.path.exists(download_dir), "Файл не был скачан"
    print(f"\nФайл успешно скачан: {download_dir}")


@pytest.mark.parametrize('driver', ['https://saby.ru/download'], indirect=True)
def test_file_size(driver):
    """Тест проверки размера файла"""
    down_page = DownPage(driver)
    download_dir = os.path.join(os.getcwd(), "downloads")  # Папка загрузок по умолчанию
    expected_filename = "saby-setup-web.exe"  # Ожидаемое имя файла
    file_path = os.path.join(download_dir, expected_filename)


    timeout = 30  # Максимальное время ожидания в секундах
    poll_time = 1  # Время ожидания перед повторной проверкой
    start_time = time.time()
    # Проверяем что файл существует
    while time.time() - start_time < timeout:
        if os.path.exists(file_path):
            # Проверка завершенности загрузки
            if os.path.getsize(file_path) > 0:
                break
        time.sleep(poll_time)
    else:
        raise AssertionError("Файл не был скачан вовремя или он пустой")

    # Получаем результат проверки размера
    result = down_page.verify_file_size(file_path)

    print(f"\nПроверка размера файла:")
    print(f"Ожидаемый: {result['expected'] / (1024 * 1024):.2f} МБ")
    print(f"Фактический: {result['actual'] / (1024 * 1024):.2f} МБ")

    assert result['is_match'], f"Размер файла не соответствует. Разница: {result['difference_percent']:.2f}%"

