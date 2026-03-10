import pandas as pd
from faker import Faker

fake = Faker()

data = [{
    "name": fake.name(),
    "email": fake.email(),
    "city": fake.city(),
    "job": fake.job(),
    "company": fake.company()
} for _ in range(100)]

df = pd.DataFrame(data)

df.to_csv("../generated_data/fake_users.csv", index=False)

print("CSV file generated: ../generated_data/fake_users.csv")
