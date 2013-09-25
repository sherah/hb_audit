import random

try_count = []
print "Hi. What's your name? "
name = raw_input("> ")

def generate_number():
  random_number = random.uniform(1,100)
  print "the random number is %d" % random_number
  return random_number

def ask_to_guess():
  yg = "Your guess? "
  guess = raw_input(yg)
  check_guess(guess)

def check_guess(guess):
  try_count.append(int(guess))
  if int(guess) > 100 or int(guess) < 1:
    print "I said the number has to be between 1 and 100!"
    ask_to_guess()
  elif int(guess) < int(secret_number):
    print "That number is too low."
    ask_to_guess()
  elif int(guess) > int(secret_number):
    print "That number is too high."
    ask_to_guess()
  elif int(guess) == int(secret_number):
    print "You win! The secret number was %d! It only took you %d tries too!" % (secret_number, len(try_count))

secret_number = generate_number()
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
ask_to_guess()

