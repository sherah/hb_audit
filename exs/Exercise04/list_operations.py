
"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list[1:len(input_list)]

def last(input_list):
    """Return the last element of the input list."""
    return input_list[-1]

def init(input_list):
    """Return all elements of the input list except the last."""
    return input_list[0:-1]

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list[0:3]

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list[-5:len(input_list)]

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two.
    """
    return input_list[2:-2]

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list[2:6]

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return inner_four(input_list[::-1])

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0] = 42
    return input_list

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    n = 37
    input_list[2] = n
    input_list[-1] = n
    return input_list

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """
    newlist = input_list[0:2]
    newlist.append(42)
    newlist.append(37)
    newlist.append(input_list[-2])
    newlist.append(input_list[-1])
    return newlist

def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[6]
    del input_list[2]
    return input_list

def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """
    del input_list[2:-2]
    return input_list

"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    counter = 0
    for i in input_list:
        counter += 1
    return counter

# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
    newlist = input_list + [value]
    print "custom append's newlist: %r" % newlist 
    return newlist

def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
    for i in values:
        input_list.append(i)
    return input_list

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    firstpart = input_list[0:index]
    firstmiddle = custom_append(firstpart, value)
    lastpart = input_list[index:]
    newlist = firstmiddle + lastpart
    return newlist

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
    count = 0
    firstpartindex = 0
    for i in input_list:
        if(input_list[count] == value):
          firstpartindex = count
          break
        count += 1
    firstpart = input_list[0:firstpartindex]
    lastpart = input_list[firstpartindex+1:]
    newlist = firstpart + lastpart
    return newlist

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    newlist = input_list[0:-1]
    return newlist

def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    count = 0
    for el in input_list:
        if(input_list[count] == value):
            index = count
            break
        count += 1
    return index

def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""
    count = 0
    valuecount = 0
    for el in input_list:
        if(input_list[count] == value):
            valuecount += 1
        count += 1
    return valuecount

def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""
    newlist = []
    while len(input_list) > 0:
      custom_append(newlist, input_list[-1])
      input_list = custom_pop(input_list)
      print "input list: %r" % input_list
      print "newlist: %r" % newlist
    return newlist

def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    count = 0
    for i in input_list:
        if(input_list[count] == value):
          exists = True
          break
        else:
          exists = False
        count += 1
    return exists

def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    count = 0
    if(some_list > another_list or another_list > some_list):
        return False

    for i in some_list:
        if(some_list[count] != another_list[count]):
            same = False
            break
        else:
            same = True
        count += 1
    return same
