import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from pages.about_rent import About_Rent, Links
from pages.main_page import Main_Page
from pages.scooter_page import Form_Order



class TestOrders:
    @allure.title('Проверка заказа с помощью верхней кнопки Заказать')
    def test_checkout_top_button(self, driver):
        main = Main_Page(driver)
        main.go_to_site()
        main.click_to_order_top()
        order_form = Form_Order(driver)
        order_form.input_name()
        order_form.input_address()
        order_form.input_phone()
        order_form.click_continue_button()
        continuation_of_the_order = About_Rent(driver)
        continuation_of_the_order.input_date()
        continuation_of_the_order.input_other()
        continuation_of_the_order.order_confirmation()
        text = driver.find_element(*Locators.LOCATOR_VIEW_STATUS).text
        assert text == "Посмотреть статус"

    @allure.title('Проверка заказа с помощью нижней кнопки Заказать')
    def test_checkout_low_button(self, driver):
        main = Main_Page(driver)
        main.go_to_site()
        main.scroll()
        main.click_to_order_low()
        order_form = Form_Order(driver)
        order_form.input_name()
        order_form.input_address()
        order_form.input_phone()
        order_form.click_continue_button()
        continuation_of_the_order = About_Rent(driver)
        continuation_of_the_order.input_date()
        continuation_of_the_order.input_other()
        continuation_of_the_order.order_confirmation()
        text = driver.find_element(*Locators.LOCATOR_VIEW_STATUS).text
        assert text == "Посмотреть статус"

    @allure.title('Проверка перехода по ссылке(самокат) через заказ')
    def test_link_scooter(self, driver):
        main = Main_Page(driver)
        main.go_to_site()
        main.click_to_order_top()
        link = Links(driver)
        link.links_scooter()
        url = driver.current_url
        assert url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода по ссылке(яндекс) через заказ')
    def test_link_yandex(self, driver):
        main = Main_Page(driver)
        main.go_to_site()
        main.click_to_order_top()
        link = Links(driver)
        link.links_yandex()
        current_url = driver.current_url
        assert current_url != 'https://yandex.ru/'  # проверка, что тест заведомо провальный, т.е. не переходит на страницу яндекса
