#!/bin/env python

s = """
Given a multiline string 's', print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""

s2 = s.splitlines()

for i in range(len(s2)):
	print "Line %r: %r" % (i, s2[i])

