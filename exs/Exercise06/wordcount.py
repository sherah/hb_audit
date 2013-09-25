from sys import argv
import pprint

script, filename = argv

f = open(filename)

word_count = {}
for line in f:
  words = line.split()
  for el in words:
    if(el in word_count):
      word_count[el] += 1
    else:
      word_count[el] = 1

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(word_count)
