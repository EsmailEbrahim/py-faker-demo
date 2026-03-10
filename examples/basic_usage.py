from faker import Faker

fake = Faker()

print("Name:", fake.name())
print("Email:", fake.email())
print("Address:", fake.address())
print("Company:", fake.company())
print("Date of birth:", fake.date_of_birth())
print("Phone number:", fake.phone_number())
print("Job:", fake.job())
print("Text:", fake.text())
