import allure


from pages.redirect_page import RedirectPage


class TestRedirectPage:
    @allure.title('Тест проверки перехода на главную страницу веб-приложения по клику на логотип "Самокат"')
    @allure.description('''1)кликаем на кнопку "Заказать"
                               2)Кликаем на логотип "Самокат"
                               3)Проверяем наличие текста в описании заголовка  с ожидаемым  заголовком ''')
    def test_logo_scooter_redirect(self, driver):
        redirect_page = RedirectPage(driver)
        assert 'пару дней' in redirect_page.logo_scooter_redirect()

    @allure.title('Тест проверки перехода на Яндекс.Дзен веб-приложении по клику на логотип "Яндекса"')
    @allure.description('''1)кликаем на кнопку "Яндекс"
                            2)Переходим на новую страницу браузера в Яндекс.Дзен
                            3)Проверяем отображение элемента "Главная" для подтверждения перехода ''')
    def test_ya_logo_redirect(self, driver):
        redirect_page = RedirectPage(driver)
        assert redirect_page.ya_logo_redirect().is_displayed(), "Элемент отображается на странице"