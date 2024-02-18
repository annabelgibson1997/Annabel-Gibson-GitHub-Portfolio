#Create a simple string with the content: 
#"The!quick!brown!fox!jumps!over!the!lazy!dog."
#Replace all "!" with " " by using replace() function and reprint the string.
#reprint the string in all caps, using upper() function.
#print the sentence in reverse using the slicing function.
#For this function use [::-1].

simple_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(simple_string)

simple_string = simple_string.replace("!", " ")
print(simple_string)

simple_string = simple_string.upper()
print(simple_string)

print(simple_string[::-1])