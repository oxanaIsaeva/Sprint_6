import allure
from pages.trackit_page import MainPageRedirect
from locators.trackit_page_locators import RedirectLocators
from data import RedirectExpected
from conftest import driver


class TestRedirect:

    @allure.title('Проверка, что при нажатии на логотип «Самоката», пападаешь на главную страницу «Самоката»')
    @allure.description('Сверяем текущий url с ожидаемым (data > RedirectExpected)')
    def test_redirect_to_scooter(self, driver):
        redirect = MainPageRedirect(driver)
        redirect.redirect_to_scooter(driver, RedirectLocators.SCOOTER_LOGO)

        assert driver.current_url == RedirectExpected.expected_url_scooter

    @allure.title('Проверка, что при нажатии на логотип Яндекса, пападаешь на страницу Дзена')
    @allure.description('Находим элемент на странице Дзена после редиректа')
    def test_redirect_to_dzen(self, driver):
        redirect = MainPageRedirect(driver)
        redirect.redirect_to_dzen(driver, RedirectLocators.YANDEX_LOGO)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        assert redirect.find_element_with_wait(RedirectLocators.DZEN_TEXT)
