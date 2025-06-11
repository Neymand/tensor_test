
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.contact_page import ContactPage

chrome_options = Options()
chrome_options.add_argument("--headless")

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
def test_check_region(driver):
    """
    Тестирует изменение региона на Камчатский край и проверяет, что обновился список партнеров, URL и title.
    """
    contact_page = ContactPage(driver)
    contact_page.open_contacts()
    contact_page.verify_current_region('Самарская обл.')


@pytest.mark.parametrize(
        "location, expected_url",
        [
            ("Камчатский край", "41-kamchatskij-kraj"),
            ("Мурманская обл.", "51-murmanskaya-oblast"),
            ("Тольятти", "63t-tolyatti")
        ]
    )
@pytest.mark.parametrize('driver', ['https://saby.ru/contacts'], indirect=True)
def test_change_region(driver, location, expected_url):
    contact_page = ContactPage(driver)
    contact_page.change_region(location)
    # Шаг 4: Проверить, что изменился регион и обновился список партнеров
    contact_page.verify_region_and_partners(location)

    # Проверка URL
    print(expected_url, contact_page.current_url())
    assert expected_url in contact_page.current_url(), "URL doesn't contain the expected region identifier"
    #
    print("Регион и соответствующие элементы успешно проверены.")