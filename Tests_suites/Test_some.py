import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestSomme:

    def test_sum(self):
        driver = self.driver
        driver.get('https://tcb.com.ua/login/')
        print("bla-bla-bla")
