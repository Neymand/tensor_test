
from selenium.webdriver.chrome.options import Options
import pytest
from pages.contact_page import ContactPage
from tests.test_driver import driver

chrome_options = Options()
chrome_options.add_argument("--headless")


@pytest.mark.parametrize('driver', ['https://saby.ru'], indirect=True)
def test_check_region(driver):
    """
    Проверяем соответствие региона
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
    """
    Меняем регионы, проверяем изменения на странице и изменение URL.
    :param driver:
    :param location:
    :param expected_url:
    :return:
    """
    contact_page = ContactPage(driver)
    contact_page.change_region(location)

    # Проверить, что изменился регион и обновился список партнеров
    contact_page.verify_region_and_partners(location)

    # Проверка URL
    print(expected_url, contact_page.current_url())
    assert expected_url in contact_page.current_url(), "URL не содержит ожидаемого идентификатора региона"
