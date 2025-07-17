class Sweet:
    def __init__(self, sweet_id, name, category, price, quantity):
        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.id} - {self.name} ({self.category}) - ₹{self.price} x {self.quantity}"
