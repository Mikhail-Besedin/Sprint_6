import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage



class OrderPage(BasePage):
    @allure.step('''Заполняем данные на странице "для кого самокат" и кликаем на кнопку "Далее" ''')
    def set_order_to_the_next_button(self, name,last_name,adress,text,tel):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR,name)
        self.add_text_to_element(OrderPageLocators.lAST_NAME_LOCATOR,last_name)
        self.add_text_to_element(OrderPageLocators.ADRESS_LOCATOR,adress)
        self.add_text_to_element(OrderPageLocators.STATION_BUTTON_LOCATOR,text)
        self.click_to_element(OrderPageLocators.ADD_STATION_LOCATOR)
        self.add_text_to_element(OrderPageLocators.TEL_LOCATOR,tel)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)

    @allure.step('''Заполняем данные на странице "Про аренду" и кликаем на кнопку "Заказать"''')
    def set_order_to_the_order_button(self,data,comment):
        self.add_text_to_element(OrderPageLocators.DATA_BUTTON,data)
        self.click_to_element(OrderPageLocators.DAY_BUTTON)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_BUTTON)
        self.click_to_element(OrderPageLocators.PERIOD_BUTTON)
        self.click_to_element(OrderPageLocators.COLOR_BUTTON)
        self.add_text_to_element(OrderPageLocators.COMMENTS_BUTTON,comment)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.YES_BUTTON)


    @allure.step('''Получаем текст из страницы  после оформления заказа''')
    def page_set_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_MODALHEADER_LOCATOR)




