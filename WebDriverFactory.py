from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:
    @staticmethod
    def create(browser_type="Chrome") -> webdriver:
        return WebDriverFactory._product_web_driver()

    @staticmethod
    def _product_web_driver() -> WebDriver:
        chrome_option = Options()
        chrome_option.binary_location = "C://webdriver"
        return webdriver.Chrome("C://", option=chrome_option)