![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
---
# py-faker-demo

Example project demonstrating how to generate **fake datasets in Python** using the Faker library.

Useful for:

* testing applications
* generating demo data
* machine learning datasets
* database seeding

---

# Installation

```bash
git clone https://github.com/EsmailEbrahim/py-faker-demo.git
cd py-faker-demo
pip install -r requirements.txt
```

---

# Basic Example

```python
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.email())
print(fake.address())
```

---

# Run Examples

```
python examples/basic_usage.py
python examples/generate_users.py
python examples/csv_export.py
python examples/json_export.py
python examples/ecommerce_example.py
python examples/large_dataset.py
```

---

# Generate Dataset via CLI

```
python generate_dataset.py --rows 1000
```

Output:

```
generated_data/generated.csv
```

---

# Example Output

| name       | email                                       | city   | job      |
| ---------- | ------------------------------------------- | ------ | -------- |
| John Smith | [john@example.com](mailto:john@example.com) | London | Engineer |

---

# Features

- Fake users
- CSV export
- JSON export
- Pandas datasets
- Relational datasets
- Locale support
- Large dataset generation
- CLI dataset generator

---

# Project Structure

```
py-faker-demo/
 ├ examples/
 ├ generated_data/
 ├ generate_dataset.py
 ├ requirements.txt
 └ README.md
```

---

# Requirements

* Python 3.8+
* faker
* pandas

---

# License

MIT License
