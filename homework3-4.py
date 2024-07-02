# Create a list of dinner guests
guests = ["Alan Turing", "Jane Austen", "Frida Kahlo"]

# Loop through the list and invite each guest
for guest in guests:
  message = f"Dear {guest}, I would be honored if you would join me for dinner. I'm a big admirer of your work in {guest.split()[1]}. It would be fascinating to discuss your thoughts and experiences."
  print(message)
