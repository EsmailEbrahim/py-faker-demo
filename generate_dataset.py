import argparse
import pandas as pd
from faker import Faker

fake = Faker()

parser = argparse.ArgumentParser(description="Generate fake datasets")
parser.add_argument("--rows", type=int, default=100)
parser.add_argument("--output", default="generated_data/generated.csv")

args = parser.parse_args()

data = [{
    "name": fake.name(),
    "email": fake.email(),
    "city": fake.city(),
    "job": fake.job(),
    "company": fake.company()
} for _ in range(args.rows)]

df = pd.DataFrame(data)

df.to_csv(args.output, index=False)

print(f"Generated {args.rows} rows → {args.output}")
