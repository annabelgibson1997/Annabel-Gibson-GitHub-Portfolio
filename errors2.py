# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # syntax: need to add "" to make the value a string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a  {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."
# logic: number_of_teeth and animal_type need to change places for the sentence to make sense.
# runtime: turned this into an f-string to improve format

print(full_spec) # syntax: need to add brackets for print function to work.
