import allure
import pytest
import data
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
        assert result == main_page.get_answer_text(num)


    @allure.title(
        'Тест проверки перехода на страницу заказа в веб-приложении по клику на кнопку  "Заказать" в хедере ')
    @allure.description('''1)кликаем на кнопку "Заказать" в хедере
                            2)Проверяем наличие текста "Для кого самокат" в описании заголовка  ''')
    def test_click_header_order_button(self,driver):
        main_page = MainPage(driver)
        assert main_page.click_header_order_button() == "Для кого самокат"

    @allure.title('Тест проверки перехода на страницу заказа в веб-приложении по клику на кнопку  "Заказать" внизу страницы ')
    @allure.description('''1)кликаем на кнопку "Заказать" внизу страницы 
                        2)Проверяем наличие текста "Для кого самокат" в описании заголовка  ''')
    def test_click_order_down_button(self,driver):
        main_page = MainPage(driver)
        assert main_page.click_order_down_button() == "Для кого самокат"
