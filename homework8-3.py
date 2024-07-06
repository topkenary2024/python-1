def make_shirt(size='large', message='I love Python!'):
  """Prints a summary of the shirt size and message."""
  print(f"I'm making a {size.upper()} t-shirt with '{message}' printed on it.")

# Positional arguments
make_shirt('medium', 'Python is awesome!')

# Keyword arguments
make_shirt(message="Data Science Rocks!", size="small")
