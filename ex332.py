def iteration_num(rang, inc):

	numbers = []
	for i in range(0, rang):
		print "At the top i is %d" % i
		numbers.append(i)

		i += inc

		print "Numbers now: ", numbers 
		print " At the bottom i is %d" % i


iteration_num(6, 1)