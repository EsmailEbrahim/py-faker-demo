from faker import Faker
import random
import json

fake = Faker()

users = []
orders = []

# create users
for i in range(5):
    user_id = fake.uuid4()

    users.append({
        "id": user_id,
        "name": fake.name(),
        "email": fake.email()
    })

    # each user gets 1–3 orders
    for _ in range(random.randint(1, 3)):
        orders.append({
            "order_id": fake.uuid4(),
            "user_id": user_id,
            "product": fake.word(),
            "price": round(random.uniform(10, 200), 2)
        })

print("USERS")
print(json.dumps(users, indent=2))

print("\nORDERS")
print(json.dumps(orders, indent=2))
