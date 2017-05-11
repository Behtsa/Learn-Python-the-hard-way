# Formaters new style 
x = "There are {} types of people.".format(10)
binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}.".format(binary, do_not)

print x
print y

print "I said: {}.".format(x)
print "I also said: '{}'.".format(y)
hilarius = False
joke_evaluation = "Isn't that joke so funny?! %r" # doubt! {} new way does not work in here !!!

print joke_evaluation % hilarius

w = "This is the left side of..."
e = "a string with a right side."

print w + e