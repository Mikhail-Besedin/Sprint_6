import allure

from locators.main_page_locators import MainPageLocators
from locators.redirect_page_locators import RedirectPageLocators
from pages.base_page import BasePage


class RedirectPage(BasePage):
    @allure.step(''' Кликаем на кнопку "Заказать" в хедере, дальше кликаем по лого самоката,
                  получаем текст в описании заголовка на главной странице''')
    def logo_scooter_redirect(self):
        self.click_to_element(MainPageLocators.HEADER_ORDER_BUTTON)
        self.click_to_element(RedirectPageLocators.LOGO_SCOOTER)
        return self.get_text_from_element(MainPageLocators.TITLE_HOME_LOCATOR)

    @allure.step(
        ''' Кликаем на кнопку "Яндекс" в хедере,
         Переключаемся другое окно браузера и ожидаем чтобы элемент "Главная" стал видимым ''')
    def ya_logo_redirect(self):
        self.click_to_element(RedirectPageLocators.YA_LOGO)
        self.switch_to_window()
        dzen_element = self.find_element_with_wait(RedirectPageLocators.DZEN_LOCATOR)
        return dzen_element