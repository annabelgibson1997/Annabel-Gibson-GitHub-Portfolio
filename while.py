# write a program that continually asks the user to enter a number
# when the user enters -1, the program should stop requesting the user to enter a number
# then calculate the average of the numbers entered, excluding the -1

total = 0
total_attempts = 0
user_number = int(input("Enter a random number. "))

# make a rule that if the user does not write -1, they will be asked for another number
while user_number != -1:
    total += user_number # adding the numbers all together to help find the average later
    total_attempts += 1 # tallying up the number of attempts to help work out the average later
    user_number = int(input("Enter a random number. "))

    if user_number == -1:
        break 

# find average of all numbers here
average = total / total_attempts
print(f"The average of your chosen numbers is {average}.")