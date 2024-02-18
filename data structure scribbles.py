'''
# data structure scribbles

# create a list
string_list = ["John", "Mary", "Harry"]
print(string_list)

# index a list
pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
print(pet_list[0])

# slice a list
num_list = [1, 4, 2, 7, 5, 9]
print(num_list[1:2])

# change an element in a list
name_list = ["John", "Mary", "Harry"]
name_list[2] = "Tom"
print(name_list)

# add an element to a list
new_list = [34, 35, 75, "coffee", 98.8]
new_list.append("tea")
print(new_list)

#delete an element in a list
char_list = ['P', 'y', 't', 'h', 'o', 'n']
del char_list[3]
print(char_list)
'''
'''
num_list = ['1', '2', '3', '4', '5', '6'] # creating a list of numbers that are currently strings (due to quotation marks)
print(num_list)
new_num_list_ints = [int(element) for element in num_list] # making the numbers integers
print(new_num_list_ints)

# multiply every element of new_num_list_ints by 2
by_two_num_list = new_num_list_ints * 2 # WRONG - this makes the list appear twice
print(by_two_num_list) # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

# use list comprehension
by_two_num_list = [i * 2 for i in new_num_list_ints]
print(by_two_num_list) #success!! [2, 4, 6, 8, 10, 12]
'''
'''
my_tuple = (1, "apple") # understanding the tuple, a different way of creating a dictionary
key, value = my_tuple # this splits the key and the value from the variable
print(key)
print(value)

my_tuple = my_tuple + (2, "sausage") # working out how to add an element
print(my_tuple)
print(my_tuple[1])
print(my_tuple[3])
print(key)
print(value)
'''
'''
menu = ["coffee", "croissant", "tea", "cake"] # building a menu list 
print(len(menu)) #prints 4 (delete before you submit)
print(len(menu[1])) # prints the numbers of characters of index 1
'''


# Cafe menu
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Stock for each item
stock = {"Coffee": 50, "Tea": 30, "Sandwich": 20, "Cake": 15}

# Prices for each item
price = {"Coffee": 2.5, "Tea": 1.5, "Sandwich": 5.0, "Cake": 3.0}

# Calculate total stock worth
total_stock_worth = 0.0

# Loop through the menu items
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print the result
print(f"The total stock worth in the cafe is ${total_stock_worth:.2f}")