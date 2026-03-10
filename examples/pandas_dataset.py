import pandas as pd
from faker import Faker

fake = Faker()

data = [{
    "name": fake.name(),
    "email": fake.email(),
    "city": fake.city(),
    "job": fake.job()
} for _ in range(10)]

df = pd.DataFrame(data)
print(df)
