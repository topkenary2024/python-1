# Test 1
number = 10
print("Is number == 10? I predict True.")
print(number == 10)  # True

# Test 2
name = "Alice"
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # True (case-insensitive)

# Test 3
age = 25
print("\nIs age > 20? I predict True.")
print(age > 20)  # True

# Test 4
flavor = "chocolate"
print("\nIs flavor != 'vanilla'? I predict True.")
print(flavor != 'vanilla')  # True

# Test 5
is_raining = False
print("\nIs not is_raining? I predict True.")
print(not is_raining)  # True (checks for opposite)

# Test 6 (False prediction)
shopping_list = ["bread", "milk", "eggs"]
print("\nIs 'cereal' in shopping_list? I predict True.")
print('cereal' in shopping_list)  # False (item not present)

# Test 7 (False prediction)
temperature = 30
print("\nIs temperature < 25? I predict True.")
print(temperature < 25)  # False (temperature is higher)

# Test 8
password = "secret123"
print("\nIs len(password) >= 8? I predict True.")
print(len(password) >= 8)  # True (checks password length)

# Test 9
user_level = 0
print("\nIs user_level == 0 or user_level == 1? I predict True.")
print(user_level == 0 or user_level == 1)  # True (checks either condition)

# Test 10
message = ""
print("\nIs not message? I predict True.")
print(not message)  # True (empty string evaluates to False)
