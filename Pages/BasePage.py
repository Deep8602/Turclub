import sys
from selenium.webdriver import ActionChains
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

    def add_your_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def check_text(self, element_locator, text, error='wrong text'):
        element = self.driver.find_element_by_css_selector(element_locator).text
        if text.lower() in element.lower():
            print(element)
        else:
            print(error)

    def move_mouse_to_element(self, element_locator):
        element = self.wait.until(EC.presence_of_element_located(element_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def check_present_element(self, element_locator):
        element = self.wait.until(EC.presence_of_element_located(element_locator))
        return element

    def write_in_field(self, locator_field, param):
        """ Wait for the expected input and write the text in it """
        try:
            input_field = self.wait.until(EC.presence_of_element_located(locator_field))
            input_field.send_keys(param)
            return self
        except Exception:
            print('input not found ')
            print(sys.exc_info()[1])
