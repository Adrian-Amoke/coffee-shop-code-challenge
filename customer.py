class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters long")
        self._name = value

    @property
    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        unique_coffees = []
        for order in self.orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)


