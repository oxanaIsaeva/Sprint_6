import allure
from pages.main_page import MainPage


class OrderPage(MainPage):

    @allure.step('Заполнение первой части формы заказа самоката')
    def fill_form(self, name, name_text, surname, surname_text, address, address_text, metro, metro_station,
                  phone, phone_number, next_button):
        self.set_text_to_element(name, name_text)
        self.set_text_to_element(surname, surname_text)
        self.set_text_to_element(address, address_text)
        self.click_on_element(metro)
        self.click_on_element(metro_station)
        self.set_text_to_element(phone, phone_number)
        self.click_on_element(next_button)

    @allure.step('Заполнение второй части формы заказа самоката')
    def fill_second_form(self, date_locator, date, select_date, rental_period_locator, select_period,
                         select_color_locator, comment_locator, comment_text, order_button):
        self.set_text_to_element(date_locator, date)
        self.click_on_element(select_date)
        self.click_on_element(rental_period_locator)
        self.click_on_element(select_period)
        self.click_on_element(select_color_locator)
        self.set_text_to_element(comment_locator, comment_text)
        self.click_on_element(order_button)

    @allure.step('Проверка успешного завершения заказа самоката')
    def check_success_window(self, success_window, success_text_locator):
        self.find_element_with_wait(success_window)
        text = self.get_text_from_element(success_text_locator)
        return text

    @allure.step('Flow заказа самоката')
    def check_order(self, name, name_text, surname, surname_text, address, address_text, metro, metro_station,
                    phone, phone_number, next_button, date_locator, date, select_date, rental_period_locator,
                    select_period,
                    select_color_locator, comment_locator, comment_text, order_button, yes_button, success_window,
                    success_text_locator):
        self.fill_form(name, name_text, surname, surname_text, address, address_text, metro, metro_station,
                       phone, phone_number, next_button)
        self.fill_second_form(date_locator, date, select_date, rental_period_locator, select_period,
                              select_color_locator, comment_locator, comment_text, order_button)
        self.click_on_element(yes_button)
        result = self.check_success_window(success_window, success_text_locator)
        return result
