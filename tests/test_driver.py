import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
