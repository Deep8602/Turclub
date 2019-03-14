

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Tests.BaseTest import BaseTest



class TestBasePage(BaseTest):

    def test_screenshots_five_top_baners(self):
        next_top_baner_loc = (By.CSS_SELECTOR, 'div #next1')
        directory = 'C:/Users/d.popovych/PycharmProjects/TurclubBednyajka/screenshots/'
        firstbaner = '1firstbaner.jpg'
        secondbaner = '2secondbaner.jpg'
        therdbaner = '3therdbaner.jpg'
        fourthbaner = '4fourthbaner.jpg'
        fifthbaner = '5fifthbaner.jpg'


        base_page = BasePage()
        base_page.driver.maximize_window()
        base_page.screenshot(directory, firstbaner)
        base_page.push(next_top_baner_loc)
        time.sleep(1)
        base_page.screenshot(directory, secondbaner)
        base_page.push(next_top_baner_loc)
        time.sleep(1)
        base_page.screenshot(directory, therdbaner)
        base_page.push(next_top_baner_loc)
        time.sleep(1)
        base_page.screenshot(directory, fourthbaner)
        base_page.push(next_top_baner_loc)
        time.sleep(1)
        base_page.screenshot(directory, fifthbaner)

    def test_change_language_with_cookie(self):

        base_page = BasePage()
        trevel_loc = 'li a[href="/trips/"]'

        base_page.driver.add_cookie({'name': 'googtrans', 'value': '/en'})
        base_page.driver.refresh()
        base_page.check_text(trevel_loc, 'travel', 'english does not change')

        base_page.driver.add_cookie({'name': 'googtrans', 'value': '/de'})
        base_page.driver.refresh()
        base_page.check_text(trevel_loc, 'Reise', 'german does not change')

        base_page.driver.add_cookie({'name': 'googtrans', 'value': '/uk'})
        base_page.driver.refresh()
        base_page.check_text(trevel_loc, 'Поїздки', 'ukraine does not change')





