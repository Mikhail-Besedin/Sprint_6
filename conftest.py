import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@allure.step('Инициализируем драйвер с заданными параметрами разрешения экрана и закрываем браузер после завершения теста')
@pytest.fixture(scope='function')
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=2560")
    firefox_options.add_argument("--height=1440")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()