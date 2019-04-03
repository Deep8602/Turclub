from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class FirstPage(BasePage):

    next_top_baner_loc = (By.CSS_SELECTOR, 'div #next1')
