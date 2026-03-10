from faker import Faker

Faker.seed(123)

fake = Faker()

for _ in range(10):
    print(fake.name())
