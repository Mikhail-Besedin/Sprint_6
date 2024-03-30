from selenium.webdriver.common.by import By


class RedirectPageLocators:

    YA_LOGO= By.XPATH,'//*[@class ="Header_LogoYandex__3TSOI"]'
    DZEN_LOCATOR= By.XPATH, '//a[@aria-label="Главная"]'
    LOGO_SCOOTER = By.CSS_SELECTOR, '[class*="Header_Logo"] [alt="Scooter"]'