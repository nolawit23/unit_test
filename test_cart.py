import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_cart_starts_empty(self):
        self.assertEqual(len(self.cart.items), 0)

    def test_add_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"]["price"], 1.5)
        self.assertEqual(self.cart.items["apple"]["quantity"], 1)

if __name__ == '__main__':
    unittest.main()
