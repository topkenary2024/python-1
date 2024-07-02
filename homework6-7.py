person1 = {
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "city": "New York"
}

person2 = {
    "first_name": "Bob",
    "last_name": "Johnson",
    "age": 25,
    "city": "Los Angeles"
}

person3 = {
    "first_name": "Charlie",
    "last_name": "Williams",
    "age": 40,
    "city": "Chicago"
}

# List of people
people = [person1, person2, person3]

# Loop through the list and print each person's information
for person in people:
  print(f"\nFirst Name: {person['first_name'].title()}")
  print(f"Last Name: {person['last_name'].title()}")
  print(f"Age: {person['age']}")
  print(f"City: {person['city'].title()}")
