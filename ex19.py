# defining our function who will receive 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #ident lines of code inside the function to 4 spaces
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blancket.\n"
# Here we are placing numbers directly /hard code/ on the arguments for our function
print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)
# Here we are using variables to save information that we will place later on the function arguments
print "Or, we can use vaiables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Here we are doing math on each argument
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# Here we are combining math plus the value we assigned on the variables before
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

