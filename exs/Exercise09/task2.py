#!/bin/env python

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}
keys = d.keys()
sorted_keys = sorted(keys)
for i in sorted_keys:
	print "%s, %r" % (i, d[i])

