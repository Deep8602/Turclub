import time
from Pages.FirstPage import FirstPage
from Tests.BaseTest import BaseTest


class TestFirstPage(BaseTest):

    def test_screenshots_five_top_baners(self):

        directory = 'D:/Automation/Turclub/screenshots/'
        firstbaner = '1firstbaner.jpg'
        secondbaner = '2secondbaner.jpg'
        therdbaner = '3therdbaner.jpg'
        fourthbaner = '4fourthbaner.jpg'
        fifthbaner = '5fifthbaner.jpg'

        first_page = FirstPage()
        first_page.driver.maximize_window()
        first_page.screenshot(directory, firstbaner)
        first_page.push(first_page.next_top_baner_loc)

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

    def test_change_language_with_cookie(self):
        first_page = FirstPage()
        first_page.add_your_cookie({'name': 'googtrans', 'value': '/en'})
        first_page.driver.refresh()
        first_page.check_text(first_page.trevel_loc, 'travel', 'english does not change')

        first_page.add_your_cookie({'name': 'googtrans', 'value': '/de'})
        first_page.driver.refresh()
        first_page.check_text(first_page.trevel_loc, 'Reise', 'german does not change')

        first_page.add_your_cookie({'name': 'googtrans', 'value': '/uk'})
        first_page.driver.refresh()
        first_page.check_text(first_page.trevel_loc, 'Поїздки', 'ukraine does not change')

    def test_search_input(self):

        first_page = FirstPage()
        first_page.move_mouse_to_element(first_page.search_loc)
        first_page.write_in_field(first_page.search_input_loc, 'Закарпаття')
        first_page.push(first_page.search_loc)
        first_page.check_text(first_page.third_trip_loc, 'Закарпаття')

