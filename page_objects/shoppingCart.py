from general_functions.elementFinder import ElementFinder
from selenium.webdriver.common.by import By


# Shopping cart page is opened from Main menu or Product detail page.
class ShoppingCart(object):
    subtotal_amount_xpath = '//form[@id="activeCartViewForm"]//span[contains(., "Subtotal")]'

    def __init__(self, driver):
        self.driver = driver
        self.general_function = ElementFinder(self.driver)
        self.subtotal_amount = self.driver.find_element_by_xpath(self.subtotal_amount_xpath)

    def get_subtotal_details(self):
        self.general_function.is_clickable(By.XPATH, self.subtotal_amount_xpath)
        return self.subtotal_amount.text

    def is_item_added(self, name):
        item_xpath = '//span[contains(@class, "medium sc-product-title")][contains(.,"' + name + '")]'
        return self.general_function.is_visible(By.XPATH, item_xpath)
