from selenium.common.exceptions import NoSuchElementException
from WebDriverFactory import WebDriverFactory

webdriver = WebDriverFactory().create()


def test_check_if_header_menu_is_displayed():
    header_menu = webdriver.find_element_by_css_selector("ul[class$='fixedUl_nkctac']")
    assert header_menu.is_displayed(), NoSuchElementException




