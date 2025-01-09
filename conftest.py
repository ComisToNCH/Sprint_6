import pytest
from selenium import webdriver

import constants
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_page()
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.open_page()
    return page