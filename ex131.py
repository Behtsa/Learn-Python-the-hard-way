from sys import argv

script, name, age = argv
hobby = raw_input("What's your hobby? :")

print "script", script
print "name", name
print "age", age
print "Also his hobby is: %r" % hobby