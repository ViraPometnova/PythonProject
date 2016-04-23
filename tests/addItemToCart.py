import unittest
from selenium import webdriver
from page_objects.searchResult import SearchResult
from page_objects.mainMenu import MainMenu
from utilities.windowManager import WindowManager
from page_objects.productDetails import ProductDetails
from page_objects.shoppingCart import ShoppingCart


class Test(unittest.TestCase):
    search_text = 'barbie'
    search_amount = '1'
    link_number = '1'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.amazon.com/')
        self.driver.maximize_window()

    def test_add_item_to_cart(self):
        main_menu = MainMenu(self.driver)
        main_menu.search(self.search_text)

        search_result = SearchResult(self.driver)
        result_item = search_result.get_link_text(self.link_number)

        self.assertIn(self.search_text, result_item.lower(), 'Search text should be present in first search result')

        search_result.open_link(self.link_number)

        product_details = ProductDetails(self.driver)
        product_name = product_details.get_product_title()

        self.assertIn(result_item, product_name, 'Search result item name should be the same as opened product has')

        product_details.click_add_to_cart()

        main_menu = MainMenu(self.driver)
        items_amount = main_menu.get_items_amount()

        self.assertEqual(self.search_amount, items_amount,
                         'Items amount shown in cart should be the same as added amount of products')

        main_menu.open_cart()

        shopping_cart = ShoppingCart(self.driver)

        self.assertIn('Subtotal (' + items_amount + ' item):', shopping_cart.get_subtotal_details(),
                      'Items amount in Subtotal should be the same as in cart')
        self.assertTrue(shopping_cart.is_item_added(result_item),
                        'Product added to cart should be the same as the first shown in search results')
        self.assertTrue(shopping_cart.is_item_added(product_name),
                        'Product added to cart should be the same as added to cart by customer')

    def tearDown(self):
        window_manager = WindowManager(self.driver)
        window_manager.close_all_windows()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
