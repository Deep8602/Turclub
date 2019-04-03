from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class FirstPage(BasePage):

    next_top_baner_loc = (By.CSS_SELECTOR, 'div #next1')
    trevel_loc = 'li a[href="/trips/"]'
    search_loc = (By.CSS_SELECTOR, 'div.searchbtn')
    search_input_loc = (By.CSS_SELECTOR, 'input.que_search')
    third_trip_loc = 'a[ href="/trips/?show=2129"]'

