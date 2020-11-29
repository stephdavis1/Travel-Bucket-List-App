import unittest

from models.country import *

# from models.city import *


class CountryTest(unittest.TestCase):
    def setUp(self):
        self.italy = Country("Italy", 60461826, "Italian", "Euro", "26°C")

        self.morocco = Country("Morocco", 36910560, "Arabic", "Dirham", "36°C")

    def test_can_test(self):
        self.assertEqual(True, True)

    def country_has_name(self):
        self.assertEqual("Italy", self.italy.name)
