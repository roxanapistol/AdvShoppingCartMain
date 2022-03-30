import unittest
#import adshopcart_locators as locators
import advantage_shopping_cart.adshopcart_methods as methods
#import adshopcart_methods as methods



class ShoppingCartPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_advantage_shopping_cart():
        methods.setUp()
        methods.sign_up()
        methods.check_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in()
        methods.delete_test_account()
        methods.check_homepage()
        methods.tearDown()



