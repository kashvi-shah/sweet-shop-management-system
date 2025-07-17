# tests/test_shop.py

import unittest
from sweetshop.models import Sweet
from sweetshop.shop import SweetShop

class SweetShopTestCase(unittest.TestCase):
    def setUp(self):
        self.shop = SweetShop()
        self.kaju_katli = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.gajar_halwa = Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        self.shop.add_sweet(self.kaju_katli)
        self.shop.add_sweet(self.gajar_halwa)

    def test_can_add_new_sweet(self):
        gulab_jamun = Sweet(1003, "Gulab Jamun", "Milk-Based", 40, 25)
        self.shop.add_sweet(gulab_jamun)
        self.assertEqual(len(self.shop.sweets), 3)

    def test_adding_duplicate_sweet_raises_error(self):
        with self.assertRaises(ValueError):
            self.shop.add_sweet(self.kaju_katli)

    def test_can_delete_existing_sweet(self):
        self.shop.delete_sweet(1001)
        self.assertEqual(len(self.shop.sweets), 1)

    def test_can_view_all_sweets(self):
        sweets_list = self.shop.view_sweets()
        self.assertEqual(len(sweets_list), 2)

    def test_can_search_sweet_by_name(self):
        results = self.shop.search_by_name("Halwa")
        self.assertEqual(results[0].name, "Gajar Halwa")

    def test_can_search_sweet_by_category(self):
        results = self.shop.search_by_category("Nut-Based")
        self.assertEqual(results[0].name, "Kaju Katli")

    def test_can_search_sweet_by_price_range(self):
        results = self.shop.search_by_price_range(25, 35)
        self.assertEqual(results[0].name, "Gajar Halwa")

    def test_can_sort_sweets_by_price(self):
        sorted_sweets = self.shop.sort_by_price()
        self.assertEqual(sorted_sweets[0].name, "Gajar Halwa")

    def test_can_sort_sweets_by_name(self):
        sorted_sweets = self.shop.sort_by_name()
        self.assertEqual(sorted_sweets[0].name, "Gajar Halwa")

    def test_can_purchase_sweet_when_in_stock(self):
        self.shop.purchase_sweet(1001, 5)
        self.assertEqual(self.kaju_katli.quantity, 15)

    def test_purchase_fails_when_insufficient_stock(self):
        with self.assertRaises(ValueError):
            self.shop.purchase_sweet(1002, 100)

    def test_can_restock_sweet(self):
        self.shop.restock_sweet(1002, 10)
        self.assertEqual(self.gajar_halwa.quantity, 25)

if __name__ == "__main__":
    unittest.main()
