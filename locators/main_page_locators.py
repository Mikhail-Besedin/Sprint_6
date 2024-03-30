from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    BLOCK_OF_QUESTION_LOCATOR = By.CSS_SELECTOR, '[class *="Home_FourPart"]'


    HEADER_ORDER_BUTTON = By.CSS_SELECTOR,'.Header_Nav__AGCXC > button.Button_Button__ra12g'
    ORDER_DOWN_BUTTON= By.CSS_SELECTOR, '.Home_FinishButton__1_cWm > button'
    TITLE_HOME_LOCATOR= By.XPATH, '//*[@class ="Home_Header__iJKdX"]'


