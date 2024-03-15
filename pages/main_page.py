import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Делаем клик по элементу и возвращаем текстовое содержимое элемента')
    def click_to_question_and_get_answer_text(self, locator_q, locator_a):
        self.click_on_element(locator_q)
        return self.get_text_from_element(locator_a)

    @allure.step('Проверяем, что текст соответствует ожидаемому результату')
    def check_answer(self, result, expected):
        return result == expected

    @allure.step('Делаем скролл на странице до секции с вопросами')
    def scroll_to_questions(self, driver, locator):
        element = self.find_element_with_wait(locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем кнопку "Заказать" в заголовке страницы')
    def click_on_order_in_header(self, locator_order_in_header):
        self.click_on_element(locator_order_in_header)

    @allure.step('Нажимаем кнопку "Заказать" в теле страницы')
    def click_on_order(self, locator_order, driver, locator):
        self.scroll_to_questions(driver, locator)
        self.click_on_element(locator_order)










