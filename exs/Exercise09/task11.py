#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

def check_word(word, count):
  uncapitalized_words = ['a', 'and', 'the', 'of', 'in', 'an', 'to', 'but', 'or', 'nor']

  new_word = ''
  if(word not in uncapitalized_words):
    print word 
    print 'not in list'
    new_word = word.capitalize()
  else:
    new_word = word

  if(count == 0):
    new_word = word.capitalize()

  return new_word

def title(my_title):
    
    title_words = my_title.split()
    newTitle = ""

    count = 0
    for word in title_words:
      newTitle += (check_word(word, count) + " ")
      count += 1

    return newTitle

my_title = raw_input("String to title-ize: ")
print title(my_title)

