from sys import argv
import pprint

script, filename = argv

f = open(filename)
data = f.read()

full_alphabet_count = {}
for i in data:
  if i in full_alphabet_count:
      full_alphabet_count[i] += 1
  else:
    full_alphabet_count[i] = 1

letter_count = {}
for l in full_alphabet_count:
  if(ord(l) >= 65 and ord(l) <= 90 or ord(l) >= 97 and ord(l) <= 122):
    letter_count[l] = full_alphabet_count[l]

total_letters = {}
for x in letter_count:
  if(ord(x) >= 65 and ord(x) <= 90):
    total_letters[x] = letter_count[x]
    total_letters[x] += letter_count[x.lower()]
    #convert the uppercase letter to lower case
    #find that key in letter_count, get its value, add to upper case value

pp = pprint.PrettyPrinter(indent=4)
print "All characters in this file:"
pp.pprint(full_alphabet_count)
print "Just the letters:"
pp.pprint(letter_count)
print "Letter totals:"
pp.pprint(total_letters)