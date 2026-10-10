"""Calculate shopping cart totals using one shared discount rule."""

DISCOUNT_THRESHOLD = 5000
DISCOUNT_PERCENTAGE = 10


def calculate_total(items):
    """Calculate the total price of all items in cents."""
    return sum(item.price_cents * item.qty for item in items)


def apply_discount(total):
    """Apply a 10% discount when the total is above 5000 cents."""
    if total > DISCOUNT_THRESHOLD:
        return int(total * (100 - DISCOUNT_PERCENTAGE) / 100)

    return total


def apply_discount_to_cart(cart):
    total = calculate_total(cart.items)
    return apply_discount(total)


def generate_invoice(order):
    total = calculate_total(order.items)
    total = apply_discount(total)

    invoice = f"Invoice for order {order.id}\n"
    invoice += f"Customer: {order.user_email}\n"
    invoice += f"Total (after discount if applicable): {total} cents"

    return invoice


if __name__ == "__main__":
    class Item:
        def __init__(self, price_cents, qty):
            self.price_cents = price_cents
            self.qty = qty

    class Cart:
        def __init__(self, items):
            self.items = items

    class ExampleOrder:
        def __init__(self, items):
            self.id = 1
            self.user_email = "customer@example.com"
            self.items = items

    items = [Item(3000, 2)]

    cart = Cart(items)
    order = ExampleOrder(items)

    print(apply_discount_to_cart(cart))
    print(generate_invoice(order))