# For this task imagine you are running a cafe
# Create a list called menu and have it contain 4 items sold in your cafe
# Create a dictionary called stock which will contain the stock value for each item
# Create another dictionary called price to contain all the prices for each item
# Calculate the total_stock_worth in the cafe
# To achieve this, you will need to LOOP through the appropriate dictionaries and lists
# When you loop, set the 'items' as keys 
# The keys should help access corresponding stock and price values.
# Each item value is calculated using this method item_value = (stock[items] * price[items])
# print out the result

menu = ["coffee", "croissant", "tea", "cake"] # building a menu list 

print("Welcome to Annabel's cafe. Here's whats on the menu today:\n")

for items in menu:
    print(f"- {items}") # this prints each item out in a list, with a new line for each

stock = {"coffee": 50, # building a stock dictionary, matching menu list items to the keys
         "croissant": 25,
         "tea": 103,
         "cake": 48
         }

price = {"coffee": 3.55, # building a price dictionary, matching menu list items to the keys
         "croissant": 3.0,
         "tea": 2.99,
         "cake": 3.50
         }
    
total_stock_worth = 0.0 # creating a float value (rather than integer) to consider pennies + starting the value at 0.0

print("\nIndividual stock worth:\n")

for items in menu: # iterating through each item on the menu
    item_value = stock[items] * price[items]
    item_value = round(item_value,2) # rounding this to 2 decimal points if necessary
    print(f"{items}: £ {item_value}") # checking the value of each item
    total_stock_worth += item_value

print(f"\nThe total stock worth in the cafe is £{total_stock_worth}\n") # using an f string to stay neat!

