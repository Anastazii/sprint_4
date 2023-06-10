import allure

from locators import Locators
from pages.base_page import BasePage


class Form_Order(BasePage):
    @allure.step('Ввод имени и фамилии')
    def input_name(self):
        self.find_element(Locators.LOCATOR_NAME).send_keys('Анастасия')
        self.find_element(Locators.LOCATOR_LASTNAME).send_keys('Попова')

    @allure.step('Ввод улицы + выбор метро')
    def input_address(self):
        self.find_element(Locators.LOCATOR_ADDRESS_FORM).send_keys('Ул. Бутлерова')
        self.find_element(Locators.LOCATOR_METRO_STATION).click()
        self.find_element(Locators.LOCATOR_STATION_SELECTION).click()

    @allure.step('Ввод телефона')
    def input_phone(self):
        self.find_element(Locators.LOCATOR_PHONE).send_keys('89204812742')

    @allure.step('Нажать на кнопку Далее')
    def click_continue_button(self):
        self.find_element(Locators.LOCATOR_FURTHER_BUTTON).click()
