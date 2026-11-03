import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Test", "Test", "Test", 1, 100.0))

    def test_discounted_total(self):
        self.assertEqual(80.0, self.cart.total_cost_with_discount(20))

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
