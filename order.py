class Order:
    """Store information about an order."""

    def __init__(self, user_id, user_email, items):
        self.user_id = user_id
        self.user_email = user_email
        self.items = items


class OrderRepository:
    """A simple placeholder for saving orders."""

    def __init__(self):
        self.orders = []

    def save(self, order):
        self.orders.append(order)


if __name__ == "__main__":
    order = Order(
        user_id=1,
        user_email="customer@example.com",
        items=["Book", "Pen"]
    )

    repository = OrderRepository()
    repository.save(order)

    print(f"Orders stored in memory: {len(repository.orders)}")