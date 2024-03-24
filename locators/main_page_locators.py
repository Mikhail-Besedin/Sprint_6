from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    BLOCK_OF_QUESTION_LOCATOR = By.CSS_SELECTOR, '[class *="Home_FourPart"]'


    HEADER_ORDER_BUTTON = By.CSS_SELECTOR,'.Header_Nav__AGCXC > button.Button_Button__ra12g'
    ORDER_DOWN_BUTTON= By.CSS_SELECTOR, '.Home_FinishButton__1_cWm > button'
    LOGO_SCOOTER = By.CSS_SELECTOR, '[class*="Header_Logo"] [alt="Scooter"]'
    TITLE_HOME_LOCATOR= By.XPATH, '//*[@class ="Home_Header__iJKdX"]'
    YA_LOGO= By.XPATH,'//*[@class ="Header_LogoYandex__3TSOI"]'

    DZEN_LOCATOR= By.XPATH, '//a[@aria-label="Главная"]'