class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        unique_customers = []
        for order in self.orders():
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)

