#!/bin/env python

"""
Given two dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys
eg:
    d1 = {"a":1, "b":2}
    d2 = {"a":3, "c":4}

    becomes

    d1 = {"a":3, "b":2, "c":4}
"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

d1keys = d1.keys()
d2keys = d2.keys()

d1items = d1.items()
d2items = d2.items()

d3 = d1items + d2items
sortedd3 = sorted(d3)




print sortedd3