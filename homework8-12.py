def make_sandwich(*items):
  """Prints a summary of the sandwich ingredients."""
  print("You ordered a sandwich with:")
  # Loop through the provided items and print them
  for item in items:
    print(f"- {item}")

# Call the function with different numbers of arguments
make_sandwich('bread', 'cheese', 'ham')
make_sandwich('turkey', 'avocado')
make_sandwich('peanut butter', 'jelly')
