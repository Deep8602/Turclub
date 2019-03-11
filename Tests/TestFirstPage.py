import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Tests.BaseTest import BaseTest


class TestBasePage(BaseTest):

    def test_sc(self):
        print('wtf!')
        locator = (By.CSS_SELECTOR, 'a[href="/"]')
        directory = 'C:/Users/d.popovych/PycharmProjects/TurclubBednyajka/screenshots/'
        name = 'basepage.png'
        base_page = BasePage()
        time.sleep(4)
        base_page.screenshot(directory, name)
        base_page.push(locator)
