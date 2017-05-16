# sys is a module that contains "system functionality" 
# .sys.argv is a list containing our scripts command line arguments
# This is how we add modules to our script from the Python module set.

# The argv is the 'argument variable' which holds the arguments we pass
# to our Python script when we run it.

from sys import argv
# Here we 'unpack' the argv so that we assign it to our variable
script, filename = argv
# open -> returns a file object. This is the preferred way to open a file.
txt = open(filename)

# Prints the name of the file
print "Here's your file %r:" % filename
# prints the content of the file
print txt.read()
# Asks the name of the file
print "Type the filename again: "
# we wait for the user response
file_again = raw_input(">")
# Assignes and open the file name given before
txt_again = open(file_again)
# Prints (reads) the content of the file
print txt_again.read()
