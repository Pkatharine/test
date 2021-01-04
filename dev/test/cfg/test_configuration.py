from selenium import webdriver
from sys import platform
import os

from selenium.webdriver.chrome.options import Options


class TestConfiguration:

    def get_driver(self):
        options = Options()
        options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'driver/executable/chromedriver.exe')
        return driver
