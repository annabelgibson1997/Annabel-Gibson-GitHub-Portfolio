# ** Part One **
# Write a program that reads in a string and makes alternate characters upper case and others lower case.
# make a rule using for loops to make any even character in the string uppercase
# to capitalise in increments you need to create a for loop and a new string
    
alternative_string = "The rain in Spain falls mainly on the plane." # creating a string with enough words/ characters to appreciate the effects of the task
print(alternative_string) # checking string in print
alternative_string = alternative_string.lower() # making all characers lowercase before alternating them
print(alternative_string) # printing to check this has worked
 

answer = "" # creating a new variable/ string to produce the the answer to part one
for char in range(len(alternative_string)):
    if char % 2: # if the character is even then it will be uppercase
        answer += alternative_string[char].upper() # this will ensure each character in upper or lower case is added to answer 
    else: # making sure all odd characters are lower case
        answer += alternative_string[char].lower()
 
print(answer)

# ** Part Two **
# Start with the same string but make each alternative word lower and then upper case 
# split() and join() functions will help you here.
# for task two look into turining all words in the phrase into a list and going from there.

alternative_string = "The rain in Spain falls mainly on the plane."
part_two = alternative_string.split(" ") # making the string into a list using the .split() function
print(part_two)

# next, make every even word in the list upper case using .upper() Apply a similar for loop as above.
answer_two = ""
for word in range(len(part_two)):
    if word % 2:
        answer_two += part_two[word].upper() + " " # Adding " " to make sure each word has a space between it
    else:
        answer_two += part_two[word].lower() + " "

print(answer_two) # this has achieved making every even word upper case. 
