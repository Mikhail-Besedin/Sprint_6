import allure

from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('''Заполняем данные на странице "для кого самокат" и "Про аренду" и кликаем на кнопку "Заказать",
     получая текст страницы успешного заказа ''')
    def set_order(self,name_locator, name,
                  last_name_locator,last_name,
                  adress_locator, adress,
                  station_locator,text,
                  add_station_locator,
                  tel_locator,tel,
                  button_locator,
                  data_button,data,
                  day_button,
                  rental_period, period,
                  color_button,
                  comment_button,comment,
                  order_button_locator,
                  yes_button,
                  locator
                  ):



        self.add_text_to_element(name_locator,name)
        self.add_text_to_element(last_name_locator,last_name)
        self.add_text_to_element(adress_locator,adress)
        self.add_text_to_element(station_locator,text)
        self.click_to_element(add_station_locator)
        self.add_text_to_element(tel_locator,tel)
        self.click_to_element(button_locator)
        self.add_text_to_element(data_button,data)
        self.click_to_element(day_button)
        self.click_to_element(rental_period)
        self.click_to_element(period)
        self.click_to_element(color_button)
        self.add_text_to_element(comment_button,comment)
        self.click_to_element(order_button_locator)
        self.click_to_element(yes_button)
        return self.get_text_from_element(locator)

