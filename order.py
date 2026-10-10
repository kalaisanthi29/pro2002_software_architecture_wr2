class Order:
    def __init__(self, user, db):
        self.user_id = user.id
        self.user_email = user.email
        self.db = db

    def save(self, items):
        self.db.execute(
            "INSERT INTO orders (user_id, email) VALUES (?, ?)",
            (self.user_id, self.user_email)
        )

        for item in items:
            self.db.execute(
                "INSERT INTO order_items (order_id, product, qty) VALUES (?, ?, ?)",
                (123, item.name, item.qty)
            )