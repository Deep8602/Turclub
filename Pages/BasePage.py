from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.DriverWrapper import DriverWrapper


class BasePage():

    wait_element_time = 20
    wait_page_load_time = 60

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)


    def push(self, element_locator, error='This item is not clickable'):
        """ Wait for the expected item and clicks on it """
        element = self.wait.until(EC.presence_of_element_located(element_locator), error)
        element.click()

    def screenshot(self, directory, name):
        '''Does screenshot and save in 'directori' as 'name' format'''
        self.driver.get_screenshot_as_file(directory + name)
