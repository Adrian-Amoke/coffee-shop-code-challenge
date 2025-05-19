# Coffee Shop Order System

This project models a simple coffee shop order system using Python classes. It includes representations for customers, coffees, and orders, allowing you to create and manage orders, track customers' favorite coffees, and analyze order data.

## Installation

This project uses `pipenv` for dependency management. To install the dependencies, run:

```bash
pipenv install
```

To activate the virtual environment, run:

```bash
pipenv shell
```

## Usage

The main classes in this project are:

- `Customer`: Represents a customer with a name. Customers can create orders.
- `Coffee`: Represents a type of coffee. You can get all orders and customers related to a coffee.
- `Order`: Represents an order linking a customer, a coffee, and a price.

Example usage:

```python
from customer import Customer
from coffee import Coffee

# Create customers and coffees
customer1 = Customer("Alice")
coffee1 = Coffee("Espresso")

# Create an order
order = customer1.create_order(coffee1, 3.5)

# Access orders and customers
print(coffee1.num_orders())  # Number of orders for this coffee
print(customer1.coffees())   # Coffees ordered by the customer
```

## Running Tests

Tests are located in the `tests` directory. To run the tests, use:

```bash
pipenv run pytest
```

## Project Structure

- `coffee.py`: Defines the `Coffee` class and related methods.
- `customer.py`: Defines the `Customer` class and related methods.
- `order.py`: Defines the `Order` class with validation and order management.
- `debug.py`: (Currently empty or for debugging purposes)
- `tests/`: Contains unit tests for the classes.

## License

This project does not specify a license.
