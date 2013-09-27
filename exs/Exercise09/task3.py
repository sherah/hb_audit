#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 10]
l2 = [93, 2, 23, 77, 66]

l3 = []
for i in range(len(l1)):
	if(l1[i] not in l2):
		l3.append(l1[i])
l3 += l2

print l3
