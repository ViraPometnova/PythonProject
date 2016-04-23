from general_functions.elementFinder import ElementFinder
from selenium.webdriver.common.by import By


# Main menu is always shown on the page.
class MainMenu(object):
    search_input_id = 'twotabsearchtextbox'
    search_button_css = 'input[value="Go"]'
    cart_button_id = 'nav-cart'
    cart_counter_id = 'nav-cart-count'

    def __init__(self, driver):
        self.driver = driver
        self.general_function = ElementFinder(self.driver)
        self.search_input = self.driver.find_element_by_id(self.search_input_id)
        self.search_button = self.driver.find_element_by_css_selector(self.search_button_css)
        self.cart_button = self.driver.find_element_by_id(self.cart_button_id)
        self.cart_counter = self.driver.find_element_by_id(self.cart_counter_id)

    def open_cart(self):
        self.general_function.is_clickable(By.ID, self.cart_button_id)
        self.cart_button.click()

    def search(self, text):
        self.general_function.is_clickable(By.ID, self.search_input_id)
        self.search_input.clear()
        self.search_input.send_keys(text)
        self.click_search()

    def click_search(self):
        self.general_function.is_clickable(By.CLASS_NAME, self.search_button_css)
        self.search_button.click()

    def get_items_amount(self):
        self.general_function.is_visible(By.ID, self.cart_counter_id)
        return self.cart_counter.text
