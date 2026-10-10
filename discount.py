def apply_discount_to_cart(cart):
    total = sum(item.price_cents * item.qty for item in cart.items)

    if total > 5000:
        total = int(total * 0.9)

    return total


def generate_invoice(order):
    invoice = f"Invoice for order {order.id}\nCustomer: {order.user_email}\n"

    total = sum(item.price_cents * item.qty for item in order.items)

    if total > 5000:
        total = int(total * 0.9)

    invoice += f"Total (after discount if applicable): {total} cents"
    return invoice