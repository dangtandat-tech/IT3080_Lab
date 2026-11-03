import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95),
        ]

    def test_search_by_title(self):
        result = search_by_title(self.dvds, "Star")
        self.assertEqual(["Star Wars"], [dvd.title for dvd in result])


if __name__ == "__main__":
    unittest.main()
