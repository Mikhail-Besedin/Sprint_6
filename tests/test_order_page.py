import allure
import pytest

import data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


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
        order_page.click_to_element(MainPageLocators.HEADER_ORDER_BUTTON)
        assert 'Заказ оформлен' in order_page.set_order(OrderPageLocators.NAME_LOCATOR, name,
                                                        OrderPageLocators.lAST_NAME_LOCATOR, last_name,
                                                        OrderPageLocators.ADRESS_LOCATOR, adress,
                                                        OrderPageLocators.STATION_BUTTON_LOCATOR, data.name_station,
                                                        OrderPageLocators.ADD_STATION_LOCATOR,
                                                        OrderPageLocators.TEL_LOCATOR, tel,
                                                        OrderPageLocators.NEXT_BUTTON_LOCATOR,
                                                        OrderPageLocators.DATA_BUTTON, data.day_delivery,
                                                        OrderPageLocators.DAY_BUTTON,
                                                        OrderPageLocators.RENTAL_PERIOD_BUTTON, OrderPageLocators.PERIOD_BUTTON,
                                                        OrderPageLocators.COLOR_BUTTON,
                                                        OrderPageLocators.COMMENTS_BUTTON, comment,
                                                        OrderPageLocators.ORDER_BUTTON_LOCATOR,
                                                        OrderPageLocators.YES_BUTTON,
                                                        OrderPageLocators.ORDER_MODALHEADER_LOCATOR

                                                        )


