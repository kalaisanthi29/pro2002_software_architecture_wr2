def process_order(order, user, discount_code, db, notify):

    total = 0
    for item in order.items:
        total += item.price * item.qty

    if discount_code == "VIP":
        total = total * 0.8
    elif discount_code == "FREESHIP":
        total = total - 50

    db.execute("INSERT INTO orders (user, total) VALUES (?, ?)", (user, total))

    if notify:
        print(f"Email sent to {user.email}: Your order total is {total}")