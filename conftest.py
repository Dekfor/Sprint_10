import pytest

from selenium import webdriver

from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.taxi_page import TaxiPage
from pages.order_page import OrderPage

from data.test_data import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def route_page(driver):
    return RoutePage(driver)


@pytest.fixture
def taxi_page(driver):
    return TaxiPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)