import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
       self.driver = driver

    @allure.step('Находим элемент применяя ожидание, чтобы элемент стал видимым ')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент применяя ожидание, чтобы элемент стал кликабельным ')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавляем текст в  элемент применяя ожидание, чтобы элемент стал видимым ')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем текст в  элементе применяя ожидание, чтобы элемент стал видимым ')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Форматируем локатор ')
    def format_locators(self, locator1, num):
        method, locator = locator1
        locator = locator.format(num)
        return (method, locator)

    @allure.step(' Скролим до элемента ')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)