# We aigned the number to the var at the left
people = 9
cars = 8
buses = 25
# we evaluate if cars is less than people
if cars > people:
	# in case statement above is true,it prints line below
	print "We should take the cars."
# we have a second evaluation if the first one is not true we check if cars is less than people
elif cars < people:
	#in case statement above is true we print line below
	print "We should not take the cars."
#but if at the end none of the above is true we print this last one
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."

elif buses < cars:
	print "Maybe we could take the buses"
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."