stars = "stars" # picking a 5 character word

for letter in stars: 
    print(letter)

for letter in range(len(stars)): 
    print(letter)

stars = "*************************"
for letter in stars: 
    print(letter)

# Pattern.py removed code:
# below is another way I tried to get the code to go back down again.
#beginning = 4

#if beginning == 4:
        #for i in range(0 ,4):
                #index = 4-i
                #star = "*****"
                #print(star[0:index]) # Index gets SMALLER as the loop goes on
    
#given_number = int(input("Enter a number: \n"))


#if given_number % 2==0: # If number is even. 
 #       stars = "*"
  #      for i in range(0 ,10):
     #           print(stars)
     #           stars = stars +"*"
                
#elif (given_number % 2 != 0): # If number is odd, i.e. the number divided by 2 does NOT have a remainder of 0.
#        stars = "**********"
 #       for i in range(0 ,10):
 #               index = 10-i  # i goes from 0 to 10 in this loop
 #               print(stars[0:index]) # Index gets SMALLER as the loop goes on i.e. from [0:10] to [0:1] i.e. fewer of the 10 original stars will be printed out.


#name = "Tim"        
#surname = " Jones"          
#age = 21
  
#full_message = name + surname +  " " + "is" + " "  + str(age) + " years old" 
#print (full_message)   
    


# Using ONE for loop, write code to output the star pattern in the task.


beginning = 1 #creating a starting integer so that user input is not necessary to run this code

if beginning == 1:  
        star = "*"
        for i in range(0 ,4): # for some reason if I move this number up to 5 an extra row of five stars appear at the end of the pattern?
                print(star)
                star = star + "*" # this takes care of stars going up to five
                if star == "*****":
                        for i in range (0 , 5): # is this for loop allowed because it is nested?
                                index = 5-i
                                print(star[0:index]) # Index gets SMALLER all the way to 0, ending the sequence
 