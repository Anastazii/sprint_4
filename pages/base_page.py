from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru"

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def scroll2(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_question(self, locator):
        question = self.driver.find_element(*locator)
        question.click()

    def get_answer_text(self, locator):
        answer = self.driver.find_element(*locator)
        return answer.text

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
