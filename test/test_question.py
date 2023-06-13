import allure
import pytest

from locators import Locators
from pages.main_page import Question


class TestQuestions1:
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (Locators.LOCATOR_FIRST_QUESTION, Locators.LOCATOR_ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (Locators.LOCATOR_SECOND_QUESTION, Locators.LOCATOR_ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (Locators.LOCATOR_THIRD_QUESTION, Locators.LOCATOR_ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (Locators.LOCATOR_FOURTH_QUESTION, Locators.LOCATOR_ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (Locators.LOCATOR_FIFTH_QUESTION, Locators.LOCATOR_ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (Locators.LOCATOR_SIXTH_QUESTION, Locators.LOCATOR_ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (Locators.LOCATOR_SEVENTH_QUESTION, Locators.LOCATOR_ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (Locators.LOCATOR_EIGHTH_QUESTION, Locators.LOCATOR_ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])

    @allure.title("Проверка вопросов")
    def test_question(self, driver, question_locator, answer_locator, expected_answer):
        question = Question(driver)
        question.go_to_site()
        question.scroll2()
        question.click_question(question_locator)
        answer = question.get_answer_text(answer_locator)
        assert answer == expected_answer
