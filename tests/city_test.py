import unittest

from models.city import *
from models.country import *


class CityTest(unittest.TestCase):
    def setUp(self):
        self.rome = City("Rome", "City Break", True)

        self.tangier = City("Tangier", "City Break", False)

    def test_can_test(self):
        self.assertEqual(True, True)

    def city_has_name(self):
        self.assertEqual("Rome", self.rome.name)