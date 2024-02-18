# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
# Due to the number of errors in this program, I have put my comments on new lines to make it easier to read.

print("Welcome to the error program") # syntax error: string needs to be in brackets to print.
print("\n") # syntax error: unexpected indentation and string needs to be in brackets to print.

# Variables declaring the user's age, casting the str to an int, and printing the result
# age_str = 24 removed age_str variable as it had no purpose
# syntax: unexpected indent. Also a double "==" has been changed to "=". age_Str doesn't conform to Python naming style.
# logic: removed "years old" from value to make it an integer.
age = 24
print("I'm " + str(age) + " years old.") # syntax: unexpected indent. Added spaces before and after variable. cast integer to string.

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 
# syntax: unexpected indent. runtime: removed the "" from the value to make it an integer.
# logic error: the final equation is missing 6 months! added ".5" to years_from_now
total_years = age + years_from_now # syntax: unexpected indent.

print("The total number of years: " + str(total_years)) 
# syntax error: string needs to be in brackets to print. Added a space before the total_years.
# logical: used a variable name that doesnt exist. This has been replaced with total_years variable
# runtime: Made int variable a string.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # logical: used a variable name that doesnt exist. This has been replaced with total_years variable
total_months = int(total_months) # added a line to turn total_months from a float to an integer
# this has been done due to the logic error on line 16 where I had to add .5 to correct the mathematics.
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") 
# syntax error: string needs to be in brackets to print.
# runtime error: integer needs to be turned into a string.

#HINT, 330 months is the correct answer

