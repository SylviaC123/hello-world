## Exercise from Chapter 6 of "Learn Python the Hard Way."
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
math_evaluation = "Does 4 plus 4 equal 5? %r"

print math_evaluation % hilarious

## Concatenating strings

x = "This is the left side of "
y = "a string with two sides."

print x + y
