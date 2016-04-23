from general_functions.elementFinder import ElementFinder
from selenium.webdriver.common.by import By
from utilities.windowManager import WindowManager


# Search result page is shown after performing search.
class SearchResult(object):
    def __init__(self, driver):
        self.driver = driver
        self.general_function = ElementFinder(self.driver)

    # number - number of link on page to be returned (starts from 0 to 17)
    def get_link_text(self, number):
        link_xpath = '//li[@id="result_' + number + '"]//h2'
        self.link = self.driver.find_element_by_xpath(link_xpath)
        self.general_function.is_clickable(By.XPATH, link_xpath)
        return self.link.text

    def open_link(self, number):
        link_xpath = '//li[@id="result_' + number + '"]//h2'
        self.link = self.driver.find_element_by_xpath(link_xpath)
        self.general_function.is_clickable(By.XPATH, link_xpath)
        self.link.click()
        window_manager = WindowManager(self.driver)
        window_manager.switch_to_last_opened_window()
