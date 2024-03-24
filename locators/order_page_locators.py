from selenium.webdriver.common.by import By


class OrderPageLocators:
    TITLE_FORM_LOCATOR= By.XPATH, "//*[contains(@class,'Order_Header__BZXOb')]"

    NAME_LOCATOR= By.XPATH, "// input[@placeholder = '* Имя']"
    lAST_NAME_LOCATOR= By.XPATH,"// input[@placeholder = '* Фамилия']"
    ADRESS_LOCATOR= By.XPATH,"// input[@placeholder = '* Адрес: куда привезти заказ']"
    STATION_BUTTON_LOCATOR= By.XPATH, "//input[@placeholder = '* Станция метро']"
    ADD_STATION_LOCATOR= By.XPATH, "//div[text() = 'Парк культуры']"
    TEL_LOCATOR= By.XPATH,"// input[@placeholder = '* Телефон: на него позвонит курьер']"
    NEXT_BUTTON_LOCATOR= By.XPATH,"// *[text() = 'Далее']"

    DATA_BUTTON= By.XPATH,"// input[@placeholder = '* Когда привезти самокат']"
    DAY_BUTTON= By.XPATH,'//div[@aria-label="Choose суббота, 30-е марта 2024 г."]'
    RENTAL_PERIOD_BUTTON= By.XPATH,"//div[@class ='Dropdown-root']"
    PERIOD_BUTTON= By.XPATH,"// *[text() = 'двое суток']"
    COLOR_BUTTON= By.XPATH,"// input[@ id='black']"
    COMMENTS_BUTTON= By.XPATH,"// input[@ placeholder = 'Комментарий для курьера']"
    ORDER_BUTTON_LOCATOR = By.CSS_SELECTOR, "div[class='Order_Buttons__1xGrp']>button:nth-child(2)"
    ORDER_MODALHEADER_LOCATOR= By.XPATH,"//*[contains(@class,'Order_ModalHeader__3FDaJ')]" # Заголовок в всплывающем окне
    YES_BUTTON= By.XPATH,"// button[text() = 'Да']"
