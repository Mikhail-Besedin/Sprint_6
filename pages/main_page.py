import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step(' Получаем текст ответа ')
    def get_answer_text(self, num):
        self.scroll_to_element(MainPageLocators.BLOCK_OF_QUESTION_LOCATOR)
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element((locator_q_formatted))
        return self.get_text_from_element(locator_a_formatted)

    @allure.step(' Кликаем на кнопку "Заказать" в хедере и получаем текст в описании заголовка ')
    def click_header_order_button(self):
        self.click_to_element((MainPageLocators.HEADER_ORDER_BUTTON))
        return self.get_text_from_element(OrderPageLocators.TITLE_FORM_LOCATOR)

    @allure.step(' Кликаем на кнопку "Заказать" внизу страницы и получаем текст в описании заголовка ')
    def click_order_down_button(self):
        self.scroll_to_element(MainPageLocators.BLOCK_OF_QUESTION_LOCATOR)
        self.click_to_element((MainPageLocators.ORDER_DOWN_BUTTON))
        return self.get_text_from_element(OrderPageLocators.TITLE_FORM_LOCATOR)