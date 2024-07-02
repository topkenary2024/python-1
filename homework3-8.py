# Create a travel wishlist (not alphabetical order)
travel_wishlist = ["Great Barrier Reef", "Macchu Picchu", "Iceland", "Galapagos Islands", "Petra"]

# Print the original list (raw)
print("Original list:", travel_wishlist)

# Print the list sorted alphabetically (using sorted() without modifying original list)
print("\nSorted alphabetically (copy):", sorted(travel_wishlist))

# Print the original list again to show it's unchanged
print("\nOriginal list (unchanged):", travel_wishlist)

# Print the list sorted reverse alphabetically (using sorted() without modifying original list)
print("\nSorted reverse alphabetically (copy):", sorted(travel_wishlist, reverse=True))

# Print the original list again to show it's unchanged
print("\nOriginal list (unchanged):", travel_wishlist)

# Reverse the order of the original list (using reverse())
travel_wishlist.reverse()
print("\nReversed list:", travel_wishlist)

# Reverse the order of the original list again (using reverse())
travel_wishlist.reverse()
print("\nOriginal order restored:", travel_wishlist)

# Sort the original list alphabetically (using sort())
travel_wishlist.sort()
print("\nSorted alphabetically (modified):", travel_wishlist)

# Sort the original list reverse alphabetically (using sort())
travel_wishlist.sort(reverse=True)
print("\nSorted reverse alphabetically (modified):", travel_wishlist)
