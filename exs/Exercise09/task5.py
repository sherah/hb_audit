#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""
s = "Hi there, my name is Slim"
y = len(s)
s2 = s[0:6] + s[12:]

print s2
