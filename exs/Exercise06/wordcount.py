from sys import argv
import pprint
import operator

script, filename = argv

f = open(filename)
removechars = ',./?><;:\'\"{}|!@#$%^&*()_-+=~`'

word_count = {}
for line in f:
  words = line.split()
  for el in words:
    el = el.lower()
    el = ''.join(x for x in el if x not in removechars)
    if(el in word_count):
      word_count[el] += 1
    else:
      word_count[el] = 1

pp = pprint.PrettyPrinter(indent=4)

print "Choose the way you want to see the data:"
print "1: sorted by frequency"
print "2: sorted alphabetically and by frequency"
print "3: just alphabetically"
display = raw_input("> ")

if(display == '1'):
  word_count_by_freq = sorted(word_count.iteritems(), key=operator.itemgetter(1), reverse=True)
  pp.pprint(word_count_by_freq)
elif(display == '2'):
  print "OKAY"
elif(display == '3'):
  pp.pprint(word_count)
else:
  print "that wasn't an option, you reject. Bye."
