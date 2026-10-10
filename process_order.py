"""Process orders using separate functions for each responsibility."""


def calculate_total(items):
    """Calculate the total price of all items."""
    return sum(item.price * item.qty for item in items)


def apply_order_discount(total, discount_code):
    """Apply a discount based on the discount code."""
    if discount_code == "VIP":
        return total * 0.8

    if discount_code == "FREESHIP":
        return total - 50

    return total


def save_order(user, total, repository):
    """Save an order using a simple repository placeholder."""
    repository.save(user, total)


def notify_user(user, total):
    """Simulate sending an order confirmation."""
    print(f"Email sent to {user.email}: Your order total is {total}")


def process_order(order, user, discount_code, repository, notify):
    """Process an order by calling smaller functions."""
    total = calculate_total(order.items)
    total = apply_order_discount(total, discount_code)

    save_order(user, total, repository)

    if notify:
        notify_user(user, total)

    return total


class OrderRepository:
    """Store orders in memory instead of using a real database."""

    def __init__(self):
        self.orders = []

    def save(self, user, total):
        self.orders.append({"user": user, "total": total})


if __name__ == "__main__":
    class Item:
        def __init__(self, price, qty):
            self.price = price
            self.qty = qty

    class User:
        def __init__(self, email):
            self.email = email

    class ExampleOrder:
        def __init__(self, items):
            self.items = items

    user = User("customer@example.com")
    order = ExampleOrder([Item(100, 2)])
    repository = OrderRepository()

    process_order(order, user, "VIP", repository, True)
    print(f"Orders stored in memory: {len(repository.orders)}")