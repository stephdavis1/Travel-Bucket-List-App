import unittest

from models.city import *
from models.country import *


class CityTest(unittest.TestCase):
    def setUp(self):
        self.italy = Country("Italy", 60461826, "Italian", "Euro", "26°C")
        self.morocco = Country("Morocco", 36910560, "Arabic", "Dirham", "36°C")

        self.rome = City("Rome", "City Break", self.italy)
        self.tangier = City("Tangier", "City Break", self.morocco)

    def test_can_test(self):
        self.assertEqual(True, True)

    def city_has_name(self):
        self.assertEqual("Rome", self.rome.name)