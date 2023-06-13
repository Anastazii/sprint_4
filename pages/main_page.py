import allure

from locators import Locators
from pages.base_page import BasePage


class Question(BasePage):
    @allure.step('Нажать на Первый вопрос + нажать на Куки')
    def first_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_FIRST_QUESTION).click()

    @allure.step('Нажать на Второй вопрос + нажать на Куки')
    def second_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_SECOND_QUESTION).click()

    @allure.step('Нажать на Третий вопрос + нажать на Куки')
    def third_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_THIRD_QUESTION).click()

    @allure.step(' Нажать на Четвертый вопрос + нажать на Куки')
    def fourth_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_FOURTH_QUESTION).click()

    @allure.step('Нажать на Пятый вопрос + нажать на Куки')
    def fifth_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_FIFTH_QUESTION).click()

    @allure.step('Нажать на Шестой вопрос + нажать на Куки')
    def sixth_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_SIXTH_QUESTION).click()

    @allure.step('Нажать на седьмой вопрос + нажать на Куки')
    def seventh_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_SEVENTH_QUESTION).click()

    @allure.step('Нажать на восьмой вопрос + нажать на Куки')
    def eighth_question(self):
        self.find_element(Locators.LOCATOR_COOKIE_BUTTON).click()
        self.find_element(Locators.LOCATOR_EIGHTH_QUESTION).click()

    def scroll2(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_question(self, locator):
        question = self.driver.find_element(*locator)
        question.click()

    def get_answer_text(self, locator):
        answer = self.driver.find_element(*locator)
        return answer.text

class Main_Page(BasePage):
    @allure.step('Нажать на верхнюю кнопку Заказать')
    def click_to_order_top(self):
        self.find_element(Locators.LOCATOR_TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на нижнюю кнопку Заказать')
    def click_to_order_low(self):
        self.find_element(Locators.LOCATOR_LOW_ORDER_BUTTON).click()

    def scroll(self):
        element = self.find_element(Locators.LOCATOR_LOW_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


