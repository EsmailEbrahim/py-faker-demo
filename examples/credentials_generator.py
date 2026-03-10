from faker import Faker

fake = Faker()

for _ in range(5):
    print({
        "username": fake.user_name(),
        "password": fake.password(),
        "email": fake.email()
    })
