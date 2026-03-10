from faker import Faker
import random

fake = Faker()

orders = []

for _ in range(5):
    orders.append({
        "order_id": fake.uuid4(),
        "customer": fake.name(),
        "product": fake.word(),
        "price": round(random.uniform(10, 500), 2),
        "date": fake.date_this_year()
    })

for order in orders:
    print(order)
