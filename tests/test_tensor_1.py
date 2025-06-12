import pytest
from pages.home_page import HomePage
from pages.tensor_page import TensorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from tests.test_driver import driver

chrome_options = Options()
chrome_options.add_argument("--headless")


@pytest.mark.parametrize('driver', ['https://saby.ru'], indirect=True)
def test_navigation_to_tensor_page(driver):
    """
    Тестирует навигацию к странице "Tensor" через интерфейс домашней страницы.
    Проверяет, что URL-адрес корректно переключился на tensor.ru после навигации.
    """
    home_page = HomePage(driver)
    home_page.go_to_contacts()
    assert driver.current_url.startswith("https://tensor.ru")


@pytest.mark.parametrize('driver', ['https://tensor.ru'], indirect=True)
def test_is_people_power_block_present(driver):
    """
    Тестирует наличие блока 'Сила в людях' на странице.
    Метод считает успешным нахождение блока, если не выбрасывается исключение TimeoutException.
    """
    tensor_page = TensorPage(driver)
    try:
        tensor_page.is_people_power_block_present()
        print("Блок 'Сила в людях' успешно найден на странице.")
    except TimeoutException:
        pytest.fail("Не удалось найти блок 'Сила в людях' на странице.")




@pytest.mark.parametrize('driver', ['https://tensor.ru/about'], indirect=True)
def test_work_section_images(driver):
    """
    Проверяет наличие и размеры изображений в рабочем разделе страницы "О нас" на tensor.ru.
    """
    tensor_page = TensorPage(driver)
    tensor_page.get_work_section_images()

    container = tensor_page.find_element(tensor_page.WORKING_BLOCK)

    # Собираем размеры
    images = container.find_elements(By.TAG_NAME, 'img')
    sizes = {(img.get_attribute('width'), img.get_attribute('height')) for img in images}

    # Проверяем, что все размеры одинаковы
    assert len(sizes) == 1, f"Найдены изображения разных размеров: {sizes}"
    assert sizes.pop()[0].isdigit(), "Ширина должна быть числом"



# @pytest.fixture(scope="module")
# def driver():
#     # Инициализация WebDriver
#     driver = webdriver.Chrome()  # Убедитесь, что у вас настроен драйвер для используемого браузера
#     yield driver
#     driver.quit()
#
# def test_navigation_to_tensor_page(driver):
#     home_page = HomePage(driver)
#     home_page.go_to()
#     home_page.go_to_contacts()
#     assert driver.current_url.startswith("https://tensor.ru")
#
# def test_is_people_power_block_present(driver):
#     tensor_page = TensorPage(driver)
#     tensor_page.is_people_power_block_present()
#     # Если метод выполняется без исключений, то блок присутствует, тест считается успешным
#
# def test_work_section_images(driver):
#     tensor_page = TensorPage(driver)
#     tensor_page.get_work_section_images()
#     container = tensor_page.find_element(tensor_page.WORKING_BLOCK)
#     images = container.find_elements(By.TAG_NAME, 'img')
#     for img in images:
#         width = img.get_attribute('width')
#         height = img.get_attribute('height')
#         assert width.isdigit() and height.isdigit(), "Высота и ширина должны быть числами"