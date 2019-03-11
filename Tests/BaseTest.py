import pytest

from utilities.DriverWrapper import DriverWrapper

@pytest.mark.usefixtures('get_browser_name')
@pytest.mark.usefixtures('get_base_url')
@pytest.mark.usefixtures('get_base_host')

class BaseTest():

    def setup(self):
        self.driver = DriverWrapper.get_webdriver()
        self.driver.get('https://tcb.com.ua')

    def teardown(self):
        DriverWrapper.close_driver()
