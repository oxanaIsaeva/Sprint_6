from selenium.webdriver.common.by import By


class RedirectLocators:
    SCOOTER_LOGO = By.XPATH, ".//img[@src='/assets/scooter.svg' and @alt='Scooter']"
    YANDEX_LOGO = By.XPATH, ".//img[@src='/assets/ya.svg' and @alt='Yandex']"
    DZEN_TEXT = By.XPATH, ".//div[@class='trends-entry-desktop__title-3S' and text()='Тренды в Дзене']"

