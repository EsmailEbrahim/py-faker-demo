import pandas as pd
from faker import Faker

fake = Faker()

rows = 10000

data = [{
    "id": i,
    "name": fake.name(),
    "email": fake.email(),
    "country": fake.country(),
    "job": fake.job()
} for i in range(rows)]

df = pd.DataFrame(data)

print("Generated rows:", len(df))
