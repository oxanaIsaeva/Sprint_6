import pytest
import allure

from conftest import driver
from data import Answers
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        "locator_q, locator_a, expected_result",
        [
            [MainPageLocators.QUESTION_LOCATOR_0, MainPageLocators.ANSWER_LOCATOR_0, Answers.ANSWER_Q0],
            [MainPageLocators.QUESTION_LOCATOR_1, MainPageLocators.ANSWER_LOCATOR_1, Answers.ANSWER_Q1],
            [MainPageLocators.QUESTION_LOCATOR_2, MainPageLocators.ANSWER_LOCATOR_2, Answers.ANSWER_Q2],
            [MainPageLocators.QUESTION_LOCATOR_3, MainPageLocators.ANSWER_LOCATOR_3, Answers.ANSWER_Q3],
            [MainPageLocators.QUESTION_LOCATOR_4, MainPageLocators.ANSWER_LOCATOR_4, Answers.ANSWER_Q4],
            [MainPageLocators.QUESTION_LOCATOR_5, MainPageLocators.ANSWER_LOCATOR_5, Answers.ANSWER_Q5],
            [MainPageLocators.QUESTION_LOCATOR_6, MainPageLocators.ANSWER_LOCATOR_6, Answers.ANSWER_Q6],
            [MainPageLocators.QUESTION_LOCATOR_7, MainPageLocators.ANSWER_LOCATOR_7, Answers.ANSWER_Q7]
        ]
    )
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @allure.description('Текст из выпадающего списка сверяем с ожидаемым результатом (data > Answers)')
    def test_questions(self, driver, locator_q, locator_a, expected_result):
        main_page = MainPage(driver)
        main_page.scroll_to_questions(driver, MainPageLocators.QUESTION_TEXT)
        main_page.click_on_element(MainPageLocators.COOKIE_BUTTON)
        result = main_page.click_to_question_and_get_answer_text(locator_q, locator_a)
        assert (main_page.check_answer(result, expected_result))
