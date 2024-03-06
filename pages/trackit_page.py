import allure

from data import Redirect
from pages.base_page import BasePage


class MainPageRedirect(BasePage):

    @allure.step('Нажатие на лого Самоката')
    def redirect_to_scooter(self, driver, scooter_logo):
        driver.get(Redirect.trakit_url)
        self.click_on_element(scooter_logo)

    @allure.step('Нажатие на лого Яндекса')
    def redirect_to_dzen(self, driver, yandex_logo):
        driver.get(Redirect.trakit_url)
        self.click_on_element(yandex_logo)
