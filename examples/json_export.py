import json
from faker import Faker

fake = Faker()

users = []

for _ in range(10):
    users.append({
        "name": fake.name(),
        "email": fake.email(),
        "username": fake.user_name(),
        "address": fake.address(),
        "phone": fake.phone_number()
    })

with open("../generated_data/users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=4)

print("../generated_data/users.json generated")
