# First, get user input for city_flight, num_nights and rental_days
# Next create four functions
# Finally, print out the results

def hotel_cost(x): # all functions need to go at the top!
    y = x * 70
    return y

def plane_cost(x):
    if city_flight == "Paris":
        y = 100
        return y
    elif city_flight == "Berlin":
        y = 80
        return y
    elif city_flight == "Amsterdam":
        y = 50
        return y
    else:
        print("Please try again and select a city from the options available.")

def car_rental(x):
    y = x * 150
    return y

def holiday_cost(num_nights, city_flight, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total

print('''Hello and welcome to you total holiday cost calculator,
which will include the plane, hotel and car-rental cost. \n
Please note this calculator operates in GBP (£).''')

num_nights = int(input("How many nights will you be staying at a hotel? \n"))

city_flight = input('''\nPlease state which city you will be flying to:
- Paris
- Berlin
- Amsterdam \n''').capitalize() # capitalized so that if user enters in lower case, this wont be a problem.

rental_days = int(input("How many days will you be hiring a car for? \n"))

print("The total hotel cost is £" + str(hotel_cost(num_nights)))

print("The total flight cost is: £" + str(plane_cost(city_flight)))

print("The total cost for your car rental is: £" + str(car_rental(rental_days)))

print("The total cost of your holiday is: £" + str(holiday_cost(num_nights, city_flight, rental_days)))