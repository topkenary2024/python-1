# Buffet menu (tuple)
buffet_menu = ("Pizza", "Salad", "Pasta", "Chicken", "Ice Cream")

# Print the menu
print("\nBuffet Menu:")
for food in buffet_menu:
  print(food)

# Attempt to modify a menu item (immutable)
try:
  buffet_menu[1] = "Soup"  # This will cause an error
  print("Menu item changed successfully! (This line won't print)")
except TypeError:
  print("Menu cannot be modified. Tuples are immutable.")

# Revised menu (new tuple)
revised_menu = ("Burgers", "Fries", "Pasta", "Fish", "Cake")

# Print the revised menu
print("\nRevised Buffet Menu:")
for food in revised_menu:
  print(food)
