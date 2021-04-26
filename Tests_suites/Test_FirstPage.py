import time

import pytest

from Pages.FirstPage import FirstPage
from Tests_suites.BaseTest import BaseTest

import allure


class TestFirstPage(BaseTest):
    @allure.step
    @pytest.mark.smoke_test
    def test_screenshots_five_top_baners(self):

        directory = 'C:/Users/Deep/PycharmProjects/Turclub/screenshots/'
        firstbaner = '1firstbaner.png'
        secondbaner = '2secondbaner.png'
        therdbaner = '3therdbaner.png'
        fourthbaner = '4fourthbaner.png'
        fifthbaner = '5fifthbaner.png'

        first_page = FirstPage()

        first_page.screenshot(directory, firstbaner)
        first_page.push(first_page.next_top_baner_loc)
        time.sleep(1)
        first_page.screenshot(directory, secondbaner)
        first_page.push(first_page.next_top_baner_loc)
        time.sleep(1)
        first_page.screenshot(directory, therdbaner)
        first_page.push(first_page.next_top_baner_loc)
        time.sleep(1)
        first_page.screenshot(directory, fourthbaner)
        first_page.push(first_page.next_top_baner_loc)
        time.sleep(1)
        first_page.screenshot(directory, fifthbaner)

    # def test_change_language_with_cookie(self):
    #     first_page = FirstPage()
    #     first_page.add_your_cookie({'name': 'Admin-Language', 'value': '/en'})
    #     first_page.driver.refresh()
    #     first_page.check_text(first_page.trevel_loc, 'travel', 'english does not change')
    #
    #     first_page.add_your_cookie({'name': 'googtrans', 'value': '/de'})
    #     first_page.driver.refresh()
    #     first_page.check_text(first_page.trevel_loc, 'Reise', 'german does not change')
    #
    #     first_page.add_your_cookie({'name': 'googtrans', 'value': '/uk'})
    #     first_page.driver.refresh()
    #     first_page.check_text(first_page.trevel_loc, 'Поїздки', 'ukraine does not change')

    @allure.step
    def test_search_input(self):

        first_page = FirstPage()
        first_page.move_mouse_to_element(first_page.search_loc)
        first_page.write_in_field(first_page.search_input_loc, 'Закарпаття')
        first_page.push(first_page.search_loc)
        first_page.check_text(first_page.first_trip_loc, 'Закарпаття')

