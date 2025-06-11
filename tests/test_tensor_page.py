import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.tensor_page import TensorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
#chrome_options.add_argument("--headless")


@pytest.fixture
def driver(request):
    """
    PyTest fixture для создания и закрытия экземпляра WebDriver.
    Получает base_url из параметров теста, чтобы открывать правильную страницу.
    """
    driver = webdriver.Chrome(options=chrome_options)
    base_url = request.param
    driver.get(base_url)
    yield driver
    driver.quit()

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
    images = container.find_elements(By.TAG_NAME, 'img')

    for img in images:
        width = img.get_attribute('width')
        height = img.get_attribute('height')
        assert width.isdigit() and height.isdigit(), "Высота и ширина должны быть числами"


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

# def test_work_section_images(driver):
#     tensor_page = TensorPage(driver)
#     tensor_page.get_work_section_images()
#     container = tensor_page.find_element(tensor_page.WORKING_BLOCK)
#     images = container.find_elements(By.TAG_NAME, 'img')
#     for img in images:
#         width = img.get_attribute('width')
#         height = img.get_attribute('height')
#         assert width.isdigit() and height.isdigit(), "Высота и ширина должны быть числами"