from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui


# General functions for checking element states.
class ElementFinder(object):
    def __init__(self, driver):
        self.driver = driver

    def is_visible(self, locator_type, locator, timeout=2):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator_type, locator)))
            return True
        except TimeoutException:
            return False

    def is_clickable(self, locator_type, locator, timeout=2):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((locator_type, locator)))
            return True
        except TimeoutException:
            return False
