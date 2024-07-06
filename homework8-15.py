def print_model(model_name, formatted=False):
  """Prints a message about the model being printed."""
  if formatted:
    print(f"We are printing the {model_name.upper()} model.")
  else:
    print(f"Printing model: {model_name}")

def show_completed_models(models):
  """Prints a message listing the completed models."""
  print("The following models have been printed:")
  for model in models:
    print(f"- {model}")
