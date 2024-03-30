import allure
import pytest

import data
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrderPage:
    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' в хедере")
    @allure.description('''1)на главной странице в хедере кликаем на кнопку "Заказать";
                            2)Заполняем данные на странице "для кого самокат' и кликаем на кнопку "Далее";
                            3)Заполняем данные "Про аренду" и кликаем на кнопку "Заказать";
                            4)Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')

    @pytest.mark.parametrize(
        'name, last_name, adress,tel,comment',
        [
            ('Анна', 'Беседина','Краснокурсантская 88 ','89992223344','первый прогон'),
            ('Михаил', 'Беседин','Каснокупеческая 99 ','89993335577','второй прогон'),

        ])
    def test_place_an_order(self, driver,name, last_name, adress,tel,comment):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        order_page.set_order_to_the_next_button(name, last_name, adress, data.name_station, tel)
        order_page.set_order_to_the_order_button(data.day_delivery,comment)
        assert 'Заказ оформлен' in order_page.page_set_order()
