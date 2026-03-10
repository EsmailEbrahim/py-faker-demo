from faker import Faker

fake = Faker('ar_EG')

for _ in range(3):
    print(fake.name())
