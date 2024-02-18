#ask the user to give you a fact using the input() function.
#save the response/ value in a variable called str_manip
#calculate and print the length of str_manip
#Find the last letter of str_manip 
#replace every occurrence with '@' using replace() function
#print the last 3 characters in str_manip backwards 
#use slice method!
#create a 5 letter word that is made up of:
#the first 3 characters and the last 2 characters.
#print this

str_manip = input("tell me an interesting fact about yourself. ")

print(len(str_manip))

final_letter = str_manip[-1]
print(final_letter)

print(str_manip.replace(final_letter, "@"))

print(str_manip[:-4:-1])

new_word = str_manip[0:3] + str_manip[-2:]
print(new_word)

