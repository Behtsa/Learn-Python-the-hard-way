#Formaters old style

# Int %d assinged inside the string x
x = "There are %d types of people." % 10
# Assignes str binary to the variable with the same name
binary = "binary"
# Assignes str don't to the variable wwith the same name
do_not = "don't"
# Assignes varible binary and do_not inside of a str
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints x
print x
# Prints y
print y

# Prints the str contatenated with str x
print "I said: %r." % x
# Prints the str contatenated with y
print "I also said: '%s'." % y
# Asignes boolean value False to the variable
hilarius = False
# Assignes str to the variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints str joke_evaluation % hilarius variable
print joke_evaluation % hilarius

# Assignes text to the variable w
w = "This is the left side of..."
# Assignes text to the variable e
e = "a string with a right side."

# Concatenates str w and e
print w + e
# In Python there are many ways to concatenate, combine strings adding '+' is one way to merge two strings together making a new 
# bigger string