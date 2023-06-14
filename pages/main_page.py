import allure

from locators import Locators
from pages.base_page import BasePage


class Main_Page(BasePage):
    @allure.step('Нажать на верхнюю кнопку Заказать')
    def click_to_order_top(self):
        self.find_element(Locators.LOCATOR_TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на нижнюю кнопку Заказать')
    def click_to_order_low(self):
        self.find_element(Locators.LOCATOR_LOW_ORDER_BUTTON).click()

    def scroll(self):
        element = self.find_element(Locators.LOCATOR_LOW_ORDER_BUTTON)
        self.scroll_to(element)


