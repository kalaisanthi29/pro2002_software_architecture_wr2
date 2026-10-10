import unittest
from types import SimpleNamespace

from converter import fahrenheit_to_celsius
from order import Order, OrderRepository
from discount import apply_discount_to_cart, generate_invoice
from process_order import process_order
from process_order import OrderRepository as ProcessingRepository


class RefactoringTests(unittest.TestCase):

    def test_converter(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_order_repository(self):
        repository = OrderRepository()
        order = Order(1, "customer@example.com", ["Book"])

        repository.save(order)

        self.assertEqual(len(repository.orders), 1)

    def test_discount(self):
        item = SimpleNamespace(price_cents=3000, qty=2)
        cart = SimpleNamespace(items=[item])
        order = SimpleNamespace(
            id=1,
            user_email="customer@example.com",
            items=[item]
        )

        self.assertEqual(apply_discount_to_cart(cart), 5400)
        self.assertIn("5400 cents", generate_invoice(order))

    def test_process_order(self):
        item = SimpleNamespace(price=100, qty=2)
        order = SimpleNamespace(items=[item])
        user = SimpleNamespace(email="customer@example.com")
        repository = ProcessingRepository()

        total = process_order(order, user, "VIP", repository, False)

        self.assertEqual(total, 160)
        self.assertEqual(len(repository.orders), 1)


if __name__ == "__main__":
    unittest.main()