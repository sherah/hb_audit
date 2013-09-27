#!/bin/env python

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, and f_to_c should do the opposite
"""

def c_to_f(celsius):
	return (celsius * 9)/5 + 32

def f_to_c(fahrenheit):
    return ((fahrenheit - 32) * 5)/9

print "Welcome to the Fahrenheit/Celsius converter exercise."
print "What do you want to get back - Fahrenheit or Celsius?"

resultType = raw_input('Type F or C: ')
if(resultType == 'F'):
	startingType = 'C'
elif(resultType == 'C'):
	startingType = 'F'
else:
	"That, um, that's not a choice. Bye."

print "Ok, how many degrees %s are we talking?" % startingType
degrees = raw_input("> ")
print "Ok."

if(startingType == 'C'):
	answer = c_to_f(int(degrees))
else:
	answer = f_to_c(int(degrees))

print "%s degrees %s is %s degrees %s!" % (degrees, startingType, answer, resultType)



