# assignes 100 to cars variable
cars = 100
# assignes 4 as the maximum space inside the car
space_in_a_car = 4
# assignes 30 drivers available
drivers = 30
# assignes the number of passengers
passengers = 90
# math stating that number of cars minus number of drivers equals the cars that won't be driven 'cuz there are more pax than drivers
cars_not_driven = cars - drivers
# equals the number of drivers to the number of cars tha will be use 
cars_driven = drivers
# states cars that'll be driven per space in each car equals the maximum number of pax they can drive
carpool_capacity = cars_driven * space_in_a_car
# informs the average of people they will transport in each car to fulfill the requirement of driving 90 passengers in 30 cars
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
