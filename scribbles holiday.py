
#def hotel_cost(x): # all functions need to go at the top!
#    y = x * 10
 #   return y
    

#num_nights = int(input("How many nights will you be staying at a hotel? \n"))

print("The total hotel cost is £" + str(hotel_cost(num_nights)))

city_flight = input('''\nPlease state which city you will be flying to:
- Paris
- Berlin
- Amsterdam \n''').capitalize() 

#def plane_cost(x):
 #   if city_flight == "Paris":
  #      y = 100
   #     return y
    #elif city_flight == "Berlin":
#        y = 80
 #       return y
  #  elif city_flight == "Amsterdam":
   #     y = 50
    #    return y
    #else:
     #   print("Please try again and select a city from the options available.")

flight_total = print("The total flight cost is: £" + str(plane_cost(city_flight)))

rental_days = int(input("How many days will you be hiring a car for? \n"))

#def car_rental(x):
#    y = x * 150
#    return y

rental_total = print("The total cost for your car rental is: £" + str(car_rental(rental_days)))

def holiday_cost(num_nights, city_flight, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total

print("The total cost of your holiday is: £" + str(holiday_cost(num_nights, city_flight, rental_days)))