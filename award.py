# the task is to create a program
# it will determine what award a person will receive

# first, create variables to find the times from each event
swimming_time = int(input("What was your swimming time? (in minutes) "))
cycling_time = int(input("What was your cycling time? (in minutes) "))
running_time = int(input("What was your running time? (in minutes) "))

# next, add all the times together to create the total time

total_time = swimming_time + cycling_time + running_time
print("It took you " + str(total_time) + " minutes to complete the triathlon.")

# now create an operation to determine the award the participant receives
# based on the total_time

if total_time >= 111:
    print("Sorry, you did not qualify and will not receive an award. Better luck next time!")
elif (total_time >= 106) and (total_time <= 110):
    print("You did not meet the qualifying time of 100 minutes, but you will receive a Provincial Scroll!")
elif (total_time >= 101) and (total_time <= 105):
    print("You did not meet the qualifying time of 100 minutes, but you will receive Provincial Half Colours.")
else:
    print("Congratulations! You have qualified and will receive Provincial Colours!")