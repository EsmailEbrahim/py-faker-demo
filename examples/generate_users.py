from faker import Faker

fake = Faker()

users = []

for _ in range(5):
    user = {
        "name": fake.name(),
        "email": fake.email(),
        "username": fake.user_name(),
        "address": fake.address(),
        "phone": fake.phone_number()
    }
    users.append(user)

print(users)
