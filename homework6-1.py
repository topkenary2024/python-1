person = {
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "city": "New York"
}

# Print each piece of information with a label
for key, value in person.items():
  print(f"{key.title()}: {value}")
