import unittest

from aims.cart import MAX_NUMBERS_ORDERED, Cart
from aims.dvd import DigitalVideoDisc


def make_dvd(index):
    return DigitalVideoDisc(f"DVD {index}", "Test", "Test", 1, 1.0)


class CartTest(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for index in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(make_dvd(index)))
        self.assertFalse(cart.add_dvd(make_dvd(MAX_NUMBERS_ORDERED)))

    def test_remove_dvd(self):
        cart = Cart()
        dvd = make_dvd(1)
        cart.add_dvd(dvd)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))


if __name__ == "__main__":
    unittest.main()
