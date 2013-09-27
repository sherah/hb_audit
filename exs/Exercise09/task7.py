#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (81,20)]

#for loop iterating over l pairs:
newlist = []
for i in range(len(l)-1):
  i1 = str(l[i]).split(",")
  i2 = str(l[i+1]).split(",")
  if(i1[1] > i2[1]):
    newlist.append(l[i+1])
    newlist.append(l[i])
  else:
    newlist.append(l[i])
#if value 1 > value 2, push value 2 and then push value 1
#else push the value to the new list

print l
print newlist



