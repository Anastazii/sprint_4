import allure

from locators import Locators
from pages.base_page import BasePage


class About_Rent(BasePage):
    @allure.step('Заполняем дату и срок аренды')
    def input_date(self):
        self.find_element(Locators.LOCATOR_DATE_ENTRY_FIELD).send_keys('14.06.2023')
        self.find_element(Locators.LOCATOR_DATE_CONFIRMATION).click()
        self.find_element(Locators.LOCATOR_RENTAL_PERIOD_BUTTON).click()
        self.find_element(Locators.LOCATOR_RENTAL_PERIOD_CHOICE).click()

    @allure.step('Выбираем цвет и оставляем комментарий')
    def input_other(self):
        self.find_element(Locators.LOCATOR_COLOR_SCOOTER).click()
        self.find_element(Locators.LOCATOR_COMMENTARY).send_keys('♥')

    @allure.step('Нажимаем кнопку Заказать + кнопку Да')
    def order_confirmation(self):
        self.find_element(Locators.LOCATOR_ORDER_BUTTON).click()
        self.find_element(Locators.LOCATOR_CONFIRM_BUTTON).click()

    @allure.step('Нажимаем кнопку Посмотреть статус')
    def view_status(self):
        self.find_element(Locators.LOCATOR_VIEW_STATUS).click()

class Links(BasePage):
    @allure.step('Нажать на кнопку Самокат')
    def links_scooter(self):
        self.find_element(Locators.LOCATOR_SCOOTER).click()

    @allure.step('Нажать на кнопку Яндекс')
    def links_yandex(self):
        self.find_element(Locators.LOCATOR_YANDEX).click()
