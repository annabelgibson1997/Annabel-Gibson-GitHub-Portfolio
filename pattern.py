# Using ONE for loop, write code to output the star pattern in the task.


star = "*" #creating a starting variable so that user input is not necessary to run this code

for i in range (0, 9):
    if i < 5:
        print(star)
        star = star + "*" # this takes care of stars going up to five
    else:
        index = 9 - i # "i" in this case = 5 so the descending pattern begins as 9 - 5 which = 4 stars etc.
        print(star[0:index])
                