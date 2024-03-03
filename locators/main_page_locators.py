from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR_0 = By.XPATH, ".//div[@id='accordion__heading-0' and @class ='accordion__button']"
    ANSWER_LOCATOR_0 = By.XPATH, ".//div[@id='accordion__panel-0' and @class ='accordion__panel']"
    QUESTION_LOCATOR_1 = By.XPATH, ".//div[@id='accordion__heading-1' and @class ='accordion__button']"
    ANSWER_LOCATOR_1 = By.XPATH, ".//div[@id='accordion__panel-1' and @class ='accordion__panel']"
    QUESTION_LOCATOR_2 = By.XPATH, ".//div[@id='accordion__heading-2' and @class ='accordion__button']"
    ANSWER_LOCATOR_2 = By.XPATH, ".//div[@id='accordion__panel-2' and @class ='accordion__panel']"
    QUESTION_LOCATOR_3 = By.XPATH, ".//div[@id='accordion__heading-3' and @class ='accordion__button']"
    ANSWER_LOCATOR_3 = By.XPATH, ".//div[@id='accordion__panel-3' and @class ='accordion__panel']"
    QUESTION_LOCATOR_4 = By.XPATH, ".//div[@id='accordion__heading-4' and @class ='accordion__button']"
    ANSWER_LOCATOR_4 = By.XPATH, ".//div[@id='accordion__panel-4' and @class ='accordion__panel']"
    QUESTION_LOCATOR_5 = By.XPATH, ".//div[@id='accordion__heading-5' and @class ='accordion__button']"
    ANSWER_LOCATOR_5 = By.XPATH, ".//div[@id='accordion__panel-5' and @class ='accordion__panel']"
    QUESTION_LOCATOR_6 = By.XPATH, ".//div[@id='accordion__heading-6' and @class ='accordion__button']"
    ANSWER_LOCATOR_6 = By.XPATH, ".//div[@id='accordion__panel-6' and @class ='accordion__panel']"
    QUESTION_LOCATOR_7 = By.XPATH, ".//div[@id='accordion__heading-7' and @class ='accordion__button']"
    ANSWER_LOCATOR_7 = By.XPATH, ".//div[@id='accordion__panel-7' and @class ='accordion__panel']"
    QUESTION_TEXT = By.XPATH, './/div[contains(@class, "Home_SubHeader__zwi_E") and text()="Вопросы о важном"]'
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
    ORDER_FROM_HEADER = By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"
    ORDER_FROM_BODY = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    SCOOTER_LOGO = By.XPATH, ".//img[@src='/assets/scooter.svg' and @alt='Scooter']"
    YANDEX_LOGO = By.XPATH, ".//img[@src='/assets/ya.svg' and @alt='Yandex']"

