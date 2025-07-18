   # test_cart.py
import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_cart_starts_empty(self):
        self.assertEqual(len(self.cart.items), 0)

    def test_add_single_item(self):
        self.cart.add_item("apple", 1.0)
        self.assertEqual(self.cart.items["apple"], {"price": 1.0, "quantity": 1})

    def test_add_multiple_different_items(self):
        self.cart.add_item("apple", 1.0, 1)
        self.cart.add_item("mango", 2.0, 3)
        self.assertEqual(self.cart.items["apple"]["quantity"], 1)
        self.assertEqual(self.cart.items["mango"]["quantity"], 3)

    def test_add_same_item_multiple_times(self):
        self.cart.add_item("apple", 1.0, 1)
        self.cart.add_item("apple", 1.0, 2)
        self.assertEqual(self.cart.items["apple"]["quantity"], 3)

    def test_get_total_price(self):
        self.cart.add_item("apple", 1.0, 2)
        self.cart.add_item("mango", 2.0, 1)
        self.assertEqual(self.cart.get_total(), 4.0)

    def test_remove_item_from_cart(self):
        self.cart.add_item("apple", 1.0)
        self.cart.add_item("mango", 2.0)
        self.cart.remove_item("apple")
        self.assertNotIn("apple", self.cart.items)

if __name__ == "__main__":
    unittest.main()
