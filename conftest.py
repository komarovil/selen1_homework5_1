import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions
import sys

def pytest_addoption(parser):
    parser.addoption("--chrome", action="store", default="http://192.168.43.31/opencart/", help="chrome")
    parser.addoption("--firefox", action="store", default="http://192.168.43.31/opencart/", help="firefox")
    parser.addoption("--ie", action="store", default="http://192.168.43.31/opencart/", help="ie")


@pytest.fixture()
def chrome(request):
    return request.config.getoption("--chrome")



@pytest.fixture
def chrome_browser(request):
    options = ChromeOptions()
    options.add_argument("--headless")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture()
def chrome(request):
    return request.config.getoption("--firefox")



@pytest.fixture
def firefox_browser(request):
    options_2 = FirefoxOptions()
    options_2.add_argument("--headless")
    wd2 = webdriver.Firefox()
    request.addfinalizer(wd2.quit)
    return wd2


@pytest.fixture()
def chrome(request):
    return request.config.getoption("--ie")


@pytest.fixture
def ie_browser(request):
    options_3 = IeOptions
    options_3.add_argument("--headless")
    wd3 = webdriver.Ie()
    request.addfinalizer(wd3.quit)
    return wd3