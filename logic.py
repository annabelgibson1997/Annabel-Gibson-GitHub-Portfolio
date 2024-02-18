# This programme has been created to present a logical error.

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_address = input("Enter your address: ")

print(f"your name is {user_age}, you are {user_address} years old and you live at {user_name}.") # logical error: variables have been placed incorrectly.

print("Let's try that again...")
print(f"your name is {user_name}, you are {user_age} years old and you live at {user_address}.") # corrected version