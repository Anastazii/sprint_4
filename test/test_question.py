import allure
from selenium.webdriver.common.by import By

from pages.main_page import Question

class TestQuestion:
    def test_first_question(self, driver):
        first_question = Question(driver)
        first_question.go_to_site()
        driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);")
        first_question.first_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-0']/p").text
        assert text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_second_question(self, driver):
        second_question = Question(driver)
        second_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        second_question.second_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-1']/p").text
        assert text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def test_third_question(self, driver):
        third_question = Question(driver)
        third_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        third_question.third_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-2']/p").text
        assert text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_fourth_question(self, driver):
        fourth_question = Question(driver)
        fourth_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        fourth_question.fourth_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-3']/p").text
        assert text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_fifth_question(self, driver):
        fifth_question = Question(driver)
        fifth_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        fifth_question.fifth_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-4']/p").text
        assert text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def test_sixth_question(self, driver):
        sixth_question = Question(driver)
        sixth_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sixth_question.sixth_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-5']/p").text
        assert text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def test_seventh_question(self, driver):
        seventh_question = Question(driver)
        seventh_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        seventh_question.seventh_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-6']/p").text
        assert text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def test_eighth_question(self, driver):
        eighth_question = Question(driver)
        eighth_question.go_to_site()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        eighth_question.eighth_question()
        text = driver.find_element(By.XPATH, "//div[@id='accordion__panel-7']/p").text
        assert text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
