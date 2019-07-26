import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
import sys

@pytest.mark.skipif(not "--chrome" in sys.argv, reason="chrome")
def test_chrome(chrome_browser):
    chrome_browser.get("http://192.168.43.31/opencart/")
    assert chrome_browser.find_element_by_class_name('swiper-slide')


@pytest.mark.skipif(not "--firefox" in sys.argv, reason="firefox")
def test_firefox(firefox_browser):
    firefox_browser.get("http://192.168.43.31/opencart/")
    assert firefox_browser.find_element_by_class_name('swiper-slide')


@pytest.mark.skipif(not "--ie" in sys.argv, reason="ie")
def test_firefox(ie_browser):
    ie_browser.get("http://192.168.43.31/opencart/")
    assert ie_browser.find_element_by_class_name('swiper-slide')