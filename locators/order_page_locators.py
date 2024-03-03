from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_LOCATOR = By.XPATH, ".//input[@placeholder ='* Имя']"
    SURNAME_LOCATOR = By.XPATH, ".//input[@placeholder ='* Фамилия']"
    ADDRESS_LOCATOR = By.XPATH, ".//input[@placeholder ='* Адрес: куда привезти заказ']"
    METRO_LOCATOR = By.XPATH, ".//input[@placeholder='* Станция метро']"
    SELECT_STATION = By.XPATH, ".//li[@data-index='5']"
    SELECT_STATION_VER_2 = By.XPATH, ".//li[@data-index='2']"
    PHONE_LOCATOR = By.XPATH, ".//input[@placeholder ='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DATE_LOCATOR = By.XPATH, ".//input[@placeholder ='* Когда привезти самокат']"
    SELECT_DATE = By.XPATH, (
                   ".//div[@class ='react-datepicker__day react-datepicker__day--013 react-datepicker__day--selected']")
    SELECT_DATE_VER_2 = By.XPATH, (
        ".//div[@class ='react-datepicker__day react-datepicker__day--021 react-datepicker__day--selected']")
    SELECT_PERIOD_LOCATOR = By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"
    SELECT_PERIOD = By.XPATH, ".//div[@class='Dropdown-option' and text()='сутки']"
    SELECT_PERIOD_VER_2 = By.XPATH, ".//div[@class='Dropdown-option' and text()='трое суток']"
    SELECT_COLOR = By.XPATH, ".//input[@id='grey' and @class='Checkbox_Input__14A2w']"
    SELECT_COLOR_VER_2 = By.XPATH, ".//input[@id='black' and @class='Checkbox_Input__14A2w']"
    COMMENT_LOCATOR = By.XPATH, (".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and "
                                 "@placeholder ='Комментарий для курьера']")
    ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    TEXT_LOCATOR = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']"
    YES_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"
    SUCCESS_WINDOW_LOCATOR = By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"
    SUCCESS_TEXT_LOCATOR = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"
