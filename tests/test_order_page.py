import allure

from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import OrderData
from conftest import driver
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка заказа самоката через кнопку Заказать в заголовке, первый набор данных')
    @allure.description('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_success_order_from_header(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order_in_header(MainPageLocators.ORDER_FROM_HEADER)
        text = order_page.check_order(OrderPageLocators.NAME_LOCATOR, OrderData.FORM['name'],
                                      OrderPageLocators.SURNAME_LOCATOR, OrderData.FORM['surname'],
                                      OrderPageLocators.ADDRESS_LOCATOR, OrderData.FORM['address'],
                                      OrderPageLocators.METRO_LOCATOR, OrderPageLocators.SELECT_STATION,
                                      OrderPageLocators.PHONE_LOCATOR, OrderData.FORM['phone'],
                                      OrderPageLocators.NEXT_BUTTON, OrderPageLocators.DATE_LOCATOR,
                                      OrderData.FORM['date'], OrderPageLocators.SELECT_DATE,
                                      OrderPageLocators.SELECT_PERIOD_LOCATOR, OrderPageLocators.SELECT_PERIOD,
                                      OrderPageLocators.SELECT_COLOR, OrderPageLocators.COMMENT_LOCATOR,
                                      OrderData.FORM['comment'], OrderPageLocators.ORDER_BUTTON,
                                      OrderPageLocators.YES_BUTTON, OrderPageLocators.SUCCESS_WINDOW_LOCATOR,
                                      OrderPageLocators.SUCCESS_TEXT_LOCATOR)
        assert OrderData.expected_text in text

    @allure.title('Проверка заказа самоката через кнопку Заказать в заголовке, второй набор данных')
    @allure.description('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_success_order_from_header_ver2(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order_in_header(MainPageLocators.ORDER_FROM_HEADER)
        text = order_page.check_order(OrderPageLocators.NAME_LOCATOR, OrderData.SECOND_FORM['name'],
                                      OrderPageLocators.SURNAME_LOCATOR, OrderData.SECOND_FORM['surname'],
                                      OrderPageLocators.ADDRESS_LOCATOR, OrderData.SECOND_FORM['address'],
                                      OrderPageLocators.METRO_LOCATOR, OrderPageLocators.SELECT_STATION_VER_2,
                                      OrderPageLocators.PHONE_LOCATOR, OrderData.SECOND_FORM['phone'],
                                      OrderPageLocators.NEXT_BUTTON, OrderPageLocators.DATE_LOCATOR,
                                      OrderData.SECOND_FORM['date'], OrderPageLocators.SELECT_DATE_VER_2,
                                      OrderPageLocators.SELECT_PERIOD_LOCATOR, OrderPageLocators.SELECT_PERIOD_VER_2,
                                      OrderPageLocators.SELECT_COLOR_VER_2, OrderPageLocators.COMMENT_LOCATOR,
                                      OrderData.SECOND_FORM['comment'], OrderPageLocators.ORDER_BUTTON,
                                      OrderPageLocators.YES_BUTTON, OrderPageLocators.SUCCESS_WINDOW_LOCATOR,
                                      OrderPageLocators.SUCCESS_TEXT_LOCATOR)
        assert OrderData.expected_text in text

    @allure.title('Проверка заказа самоката через кнопку Заказать в теле страницы, первый набор данных')
    @allure.description('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_success_order_from_body(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order(MainPageLocators.ORDER_FROM_BODY, driver, MainPageLocators.ORDER_FROM_BODY)
        text = order_page.check_order(OrderPageLocators.NAME_LOCATOR, OrderData.FORM['name'],
                                      OrderPageLocators.SURNAME_LOCATOR, OrderData.FORM['surname'],
                                      OrderPageLocators.ADDRESS_LOCATOR, OrderData.FORM['address'],
                                      OrderPageLocators.METRO_LOCATOR, OrderPageLocators.SELECT_STATION,
                                      OrderPageLocators.PHONE_LOCATOR, OrderData.FORM['phone'],
                                      OrderPageLocators.NEXT_BUTTON, OrderPageLocators.DATE_LOCATOR,
                                      OrderData.FORM['date'], OrderPageLocators.SELECT_DATE,
                                      OrderPageLocators.SELECT_PERIOD_LOCATOR, OrderPageLocators.SELECT_PERIOD,
                                      OrderPageLocators.SELECT_COLOR, OrderPageLocators.COMMENT_LOCATOR,
                                      OrderData.FORM['comment'], OrderPageLocators.ORDER_BUTTON,
                                      OrderPageLocators.YES_BUTTON, OrderPageLocators.SUCCESS_WINDOW_LOCATOR,
                                      OrderPageLocators.SUCCESS_TEXT_LOCATOR)
        assert OrderData.expected_text in text

    @allure.title('Проверка заказа самоката через кнопку Заказать в теле страницы, второй набор данных')
    @allure.description('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_success_order_from_body_ver2(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order(MainPageLocators.ORDER_FROM_BODY, driver, MainPageLocators.ORDER_FROM_BODY)
        text = order_page.check_order(OrderPageLocators.NAME_LOCATOR, OrderData.SECOND_FORM['name'],
                                      OrderPageLocators.SURNAME_LOCATOR, OrderData.SECOND_FORM['surname'],
                                      OrderPageLocators.ADDRESS_LOCATOR, OrderData.SECOND_FORM['address'],
                                      OrderPageLocators.METRO_LOCATOR, OrderPageLocators.SELECT_STATION_VER_2,
                                      OrderPageLocators.PHONE_LOCATOR, OrderData.SECOND_FORM['phone'],
                                      OrderPageLocators.NEXT_BUTTON, OrderPageLocators.DATE_LOCATOR,
                                      OrderData.SECOND_FORM['date'], OrderPageLocators.SELECT_DATE_VER_2,
                                      OrderPageLocators.SELECT_PERIOD_LOCATOR, OrderPageLocators.SELECT_PERIOD_VER_2,
                                      OrderPageLocators.SELECT_COLOR_VER_2, OrderPageLocators.COMMENT_LOCATOR,
                                      OrderData.SECOND_FORM['comment'], OrderPageLocators.ORDER_BUTTON,
                                      OrderPageLocators.YES_BUTTON, OrderPageLocators.SUCCESS_WINDOW_LOCATOR,
                                      OrderPageLocators.SUCCESS_TEXT_LOCATOR)
        assert OrderData.expected_text in text


