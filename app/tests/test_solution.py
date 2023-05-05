import unittest
from routers.solution.controller import process_orders
from models.solutions import Orders
# from app.routers.solution.controller import process_orders
# from models.solutions import Orders

class TestSolution (unittest.TestCase):


    def setUp(self) -> None:
        self.orders = Orders()
        self.orders = {
            "orders": [
                {
                    "id": 1,
                    "item": "Laptop",
                    "quantity": 1,
                    "price": 999.99,
                    "status": "completed"
                },
                {
                    "id": 2,
                    "item": "Smartphone",
                    "quantity": 2,
                    "price": 499.95,
                    "status": "pending"
                },
                {
                    "id": 3,
                    "item": "Headphones",
                    "quantity": 3,
                    "price": 99.90,
                    "status": "completed"
                },
                {
                    "id": 4,
                    "item": "Mouse",
                    "quantity": 4,
                    "price": -24.99,
                    "status": "canceled"
                }
            ]
        }

        self.dataset_result = (
            ((self.orders, "all"), 1624.83),
            ((self.orders, "completed"), 1099.89),
            ((self.orders, "pending"), 499.95),
            ((self.orders, "canceled"), 24.99),
            ((self.orders, ""), 1624.83)
        )

    def test_process_orders (self):
        for data in self.dataset_result:
            result = process_orders(*data[0])

            self.assertEqual(result, data[1])

if __name__ == '__main__':
    unittest.main()