import allure

from pages.about_rent import Links
from pages.main_page import Main_Page


class TestLink:
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