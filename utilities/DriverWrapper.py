import os

from selenium import webdriver

import WebDrivers
from utilities import settings


class DriverWrapper(object):
    _instance = None

    @classmethod
    def get_webdriver(cls):
        if not cls._instance:
            cls._instance = DriverWrapper()
            cls._driver = cls._instance._driver
        return cls._driver


    def __init__(self):
        webdrivers_path = os.path.dirname(WebDrivers.__file__)
        browser_name = settings.browser_name

        if browser_name == 'Chrome':
            options = webdriver.ChromeOptions()
            drivers_path = os.path.join(webdrivers_path, "chromedriver.exe")
            options.add_argument('--start-maximized')
            self._driver = webdriver.Chrome(executable_path=drivers_path, chrome_options=options)
            self._driver.set_page_load_timeout(60)


        if browser_name == "IE":
            drivers_path = os.path.join(webdrivers_path, "IEDriverServer_32.exe")
            self._driver = webdriver.Ie(executable_path=drivers_path)

    @classmethod
    def close_driver(cls):
        cls._driver.close()
        cls._driver.quit()
        cls._instance = None
