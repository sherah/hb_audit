#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (81,20)]

secondList = []

def flip_tuples(l):
  newList = []
  for t in l:
    firstT = t[0]
    secondT = t[1]
    newTuple = (secondT, firstT)
    newList.append(newTuple)
  return newList

#flip the tuples
secondList = flip_tuples(l)

#sort
sorted_secondList = sorted(secondList)

#flip them back
finalList = flip_tuples(sorted_secondList)


print l
print finalList



