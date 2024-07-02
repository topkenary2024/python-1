# Counting from 1 to 20
numbers = list(range(1, 21))

for number in numbers:
  print(number)

# Print the first three items
print("\nThe first three items in the list are:")
print(numbers[:3])  # Slice from the beginning to index 3 (not inclusive)

# Print three items from the middle
print("\nThree items from the middle of the list are:")
print(numbers[8:11])  # Slice from index 8 (inclusive) to 11 (not inclusive)

# Print the last three items
print("\nThe last three items in the list are:")
print(numbers[-3:])  # Slice from the end (index -3) to the end
