from general_functions.elementFinder import ElementFinder
from selenium.webdriver.common.by import By


# Product detail page is shown after user clicks on link with product name.
class ProductDetails(object):
    cart_button_id = 'add-to-cart-button'
    product_title_id = 'productTitle'

    def __init__(self, driver):
        self.driver = driver
        self.general_function = ElementFinder(self.driver)
        self.cart_button = self.driver.find_element_by_id(self.cart_button_id)
        self.product_title = self.driver.find_element_by_id(self.product_title_id)

    def click_add_to_cart(self):
        self.general_function.is_clickable(By.ID, self.cart_button_id)
        self.cart_button.click()

    def get_product_title(self):
        self.general_function.is_visible(By.ID, self.product_title_id)
        return self.product_title.text
