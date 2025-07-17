# sweetshop/shop.py

from sweetshop.models import Sweet

class SweetShop:
    def __init__(self):
        self._inventory = []

    def add_sweet(self, sweet: Sweet):
        if any(existing.id == sweet.id for existing in self._inventory):
            raise ValueError("A sweet with this ID already exists.")
        self._inventory.append(sweet)

    def delete_sweet(self, sweet_id: int):
        self._inventory = [sweet for sweet in self._inventory if sweet.id != sweet_id]

    def view_sweets(self):
        return self._inventory

    def search_by_name(self, name: str):
        return [sweet for sweet in self._inventory if name.lower() in sweet.name.lower()]

    def search_by_category(self, category: str):
        return [sweet for sweet in self._inventory if sweet.category.lower() == category.lower()]

    def search_by_price_range(self, min_price: float, max_price: float):
        return [
            sweet for sweet in self._inventory
            if min_price <= sweet.price <= max_price
        ]

    def sort_by_price(self):
        return sorted(self._inventory, key=lambda sweet: sweet.price)

    def sort_by_name(self):
        return sorted(self._inventory, key=lambda sweet: sweet.name.lower())

    def purchase_sweet(self, sweet_id: int, quantity: int):
        for sweet in self._inventory:
            if sweet.id == sweet_id:
                if sweet.quantity < quantity:
                    raise ValueError("Insufficient stock for the requested quantity.")
                sweet.quantity -= quantity
                return
        raise ValueError("Sweet not found in inventory.")

    def restock_sweet(self, sweet_id: int, quantity: int):
        for sweet in self._inventory:
            if sweet.id == sweet_id:
                sweet.quantity += quantity
                return
        raise ValueError("Sweet not found in inventory.")
