def iteration_num(rang, inc):
	i = 0
	numbers = []
	while i < rang:
		print "At the top i is %d" % i
		numbers.append(i)

		#i += 1
		i += inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


a_rang = 10
a_inc = 8

print "We can print numbers in a while loop"
iteration_num(a_rang, a_inc)

