def city_country(city, country):
  """Returns a formatted string of city and country."""
  return f"{city.title()}, {country.title()}"

# Call the function with different city-country pairs
print(city_country('london', 'england'))
print(city_country('tokyo', 'japan'))
print(city_country('taipei', 'taiwan'))
