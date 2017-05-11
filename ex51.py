# Assignes Behtsa to variable name
name = "Behtsa"
# Assignes 23 t age
age = 23
# Assignes 59 inches to variable height
height = 59 # inches
# Assignes 110 lbs to variable weight
weight = 110 # lbs
# Assignes dark brown to variable eyes color 
eyes = 'Dark brown'
# Assignes white to variable teeth color
teeth = 'White'
# Assignes dark brown to variable hair color
hair = 'Dark brown'
# Converts height given in cm
height_in_cm = height * 2.54
# Converts weight given in kg
weight_in_kg = weight * .4535

# Concatenates the variable name in the string
print "Let' talk about {}." .format (name)
# Concatenates more than just 1 variable ( height, heigh_in_cm) with the string // this with the new format
# as it can be done %d % height // %f is a float value
print "She's %d inches tall, in centimeters is %f." % (height, height_in_cm)
# Concatenates variable weight and weight_in_cm to the string
print "She's %d pounds heavy, in kilos is %f." % (weight, weight_in_kg)
# Concatenates the variables eyes and hair to the string
print "She's got %r eyes and %s hair." % (eyes, hair)
# Concatenates the variable teeth to the string below.
print "Her teeth are usually %s." % teeth

#Concatenates with .format (new way) all the variables below to the string., as a sum up
print "If I add {}, {}, and {} I get {}." .format(age, height, weight, age + height + weight)


