import allure
import pytest
import data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Тест проверки текста ответов на вопросы на главной странице веб-приложения')
    @allure.description('''1)Скроллим до блока с вопросами;
                            2)Кликаем на вопрос;
                            3)Получаем текст ответа на выбранный вопрос;
                            4)Сравниваем полученный текст с ожидаемым''')
    @pytest.mark.parametrize(
        'num, result',
        [
        (0, data.answer_text_0),
        (1, data.answer_text_1),
        (2, data.answer_text_2),
        (3, data.answer_text_3),
        (4, data.answer_text_4),
        (5, data.answer_text_5),
        (6, data.answer_text_6),
        (7, data.answer_text_7)
        ]
    )
    def test_questions_and_answer(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.BLOCK_OF_QUESTION_LOCATOR)
        assert result == main_page.get_answer_text(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,num
        )


    @allure.title(
        'Тест проверки перехода на страницу заказа в веб-приложении по клику на кнопку  "Заказать" в хедере ')
    @allure.description('''1)кликаем на кнопку "Заказать" в хедере
                            2)Проверяем наличие текста "Для кого самокат" в описании заголовка  ''')
    def test_click_header_order_button(self,driver):
        main_page = MainPage(driver)
        main_page.click_to_element((MainPageLocators.HEADER_ORDER_BUTTON))
        assert main_page.get_text_from_element(OrderPageLocators.TITLE_FORM_LOCATOR) == "Для кого самокат"

    @allure.title('Тест проверки перехода на страницу заказа в веб-приложении по клику на кнопку  "Заказать" внизу страницы ')
    @allure.description('''1)кликаем на кнопку "Заказать" внизу страницы 
                        2)Проверяем наличие текста "Для кого самокат" в описании заголовка  ''')
    def test_click_order_down_button(self,driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.BLOCK_OF_QUESTION_LOCATOR)
        main_page.click_to_element((MainPageLocators.ORDER_DOWN_BUTTON))
        assert main_page.get_text_from_element(OrderPageLocators.TITLE_FORM_LOCATOR) == "Для кого самокат"



    @allure.title('Тест проверки перехода на главную страницу веб-приложения по клику на логотип "Самокат"')
    @allure.description('''1)кликаем на кнопку "Заказать"
                                2)Кликаем на логотип "Самокат"
                                3)Проверяем наличие текста в описании заголовка  с ожидаемым  заголовком ''')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.HEADER_ORDER_BUTTON)
        main_page.click_to_element(MainPageLocators.LOGO_SCOOTER)
        assert 'пару дней'in main_page.get_text_from_element(MainPageLocators.TITLE_HOME_LOCATOR)

    @allure.title('Тест проверки перехода на Яндекс.Дзен веб-приложении по клику на логотип "Яндекса"')
    @allure.description('''1)кликаем на кнопку "Яндекс"
                        2)Переходим на новую страницу браузера в Яндекс.Дзен
                        3)Проверяем отображение элемента "Главная" для подтверждения перехода ''')
    def test_ya_logo(self,driver):
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.YA_LOGO)
        driver.switch_to.window(driver.window_handles[1])
        dzen_element = main_page.find_element_with_wait(MainPageLocators.DZEN_LOCATOR)
        assert dzen_element.is_displayed(), "Элемент отображается на странице"