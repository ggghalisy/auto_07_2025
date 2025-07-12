from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage()
    homepage.open()
    homepage.open_s6()
    productpage = ProductPage()
    productpage.check_title()
