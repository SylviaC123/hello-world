## Exercise from Chapter 14 of "Learn Python the Hard Way."
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of operating system does your computer have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking %s. You live in %r.
And you have a %r computer.
""" % (likes, lives, computer)
