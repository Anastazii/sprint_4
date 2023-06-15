import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Firefox(executable_path=r'C:\cygwin64\home\nastya\WebDriver\bin\geckodriver')
    yield browser
    browser.quit()

