#This file has been named incorrectly as saving it as "numbers.py" made the entire code become underlined by yellow squiggly lines.
#I could not run the code if I named it numbers.py - please advise!
#ask for a number
#ask for another number
#ask for one more number
#print the sum of all the numbers +
#print the first number minus the second number -
#print the third number multiplied by the first number *
#print the sum of all three numbers divided by the third + and / 

num_1 = int(input("Give me a number. "))
num_2 = int(input("Give me another number. "))
num_3 = int(input("Give me one more number. "))

answer_1 = num_1 + num_2 + num_3
print("answer one is " + str(answer_1))

answer_2 = num_1 - num_2
print("answer two is " + str(answer_2))

answer_3 = num_3 * num_1
print("answer three is " + str(answer_3))

answer_4 = answer_1 / num_3
print("answer four is " + str(answer_4))

# alternative for answer 4 below:

answer_4a = (num_1 + num_2 + num_3) / num_3
print("answer four is certainly " + str(answer_4a))

#is it bad that the answer 4 is coming out as a float rather than an integer?