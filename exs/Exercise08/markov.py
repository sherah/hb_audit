#!/usr/bin/env python

import sys
import pprint
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    twos = {}
    removechars = ',./?><;:\'\"{}|!@#$%^&*()_-+=~`'
    corpuslines = corpus.read()
    words = corpuslines.split()
    for i in range(len(words)-3):
      #ok brute forcing this...
      firstword = words[i]
      firstword = firstword.lower()
      firstword = firstword.strip(removechars)
      secondword = words[i+1]
      secondword = secondword.lower()
      secondword = secondword.strip(removechars)
      thirdword = words[i+2]
      thirdword = thirdword.lower()
      thirdword = thirdword.strip(removechars)

      #don't overwrite
      if((firstword, secondword) in twos):
        twos[firstword, secondword].append(thirdword)
      else:
        twos[firstword, secondword] = [thirdword]
    return twos

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    randomchain = ""

    def generate_phrases(chains):
      randomtext = ""
      #pick a random chain
      firstpair = chains.popitem()
      firstwords = firstpair[0]
      for word in firstwords:
        randomtext += word + " "

      secondpartchoices = firstpair[1]
      randomtext += secondpartchoices[random.randrange(0,len(secondpartchoices))]
      return randomtext

    for i in range(random.randrange(0,7)):
      randomchain += generate_phrases(chains) + " "
    
    randomchain += generate_phrases(chains) + "."

    return randomchain

def main():
    args = sys.argv

    # Change this to read input_text from a file
    script, text = args
    input_text = open(text)

    chain_dict = make_chains(input_text)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(chain_dict)
    random_text = make_text(chain_dict)
    print "Here is a random phrase generated based on the lyrical stylings of %r:" % text
    print '-***---' * 10 
    print random_text

if __name__ == "__main__":
    main()
