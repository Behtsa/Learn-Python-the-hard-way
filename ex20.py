# defining module sys who let us place argument scripts on the command line
from sys import argv
# argument input_file is the file we are gonna work with
script, input_file = argv
# Funtion: were argument f will open the input_file as call on line 19
def print_all(f):
	print f.read() # this method let us read the file pass as an argument in f

def rewind(f):
    f.seek(0) # this method is dealing in bytes, not lines. So it goes to the 0 byte (first byte) // by default. At the beginning on the file.
# line count becomes current_line as declare on line 28
def print_a_line(line_count, f): 
	print line_count, f.readline() # readline method reads one line of the file
# this means that every time we call the variable current_file we will open the input_file
current_file = open(input_file)

print "First let's print the whole file:\n"
# we call the function print all passing argument current file and will open the input_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# we will open the input_file at the beginning of the file
rewind(current_file)

print "Let's print three lines: "
#we call the print_a_line function with arguments current_file(which opens the input file)
# and argument current line which will place a counter and increase it on the lines below for 1
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
