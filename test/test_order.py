import allure

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
