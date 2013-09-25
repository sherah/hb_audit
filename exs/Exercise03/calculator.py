import arithmetic

run_calculator = True

print "Welcome to this calculator."
print "To use, type your operation first, then your numbers, separated by spaces."
print "-" * 20
print "Valid operations are:"
print "ADD: +"
print "SUBTRACT: -"
print "MULTIPLY: *"
print "DIVIDE: /"
print "SQUARE: ^2"
print "CUBE: ^3"
print "POWER OF: ^"
print "MODULUS OF: %"
print "-" * 20

def get_input():
  input = raw_input("> ")
  tokenized_input = input.split(" ")
  fn = tokenized_input.pop(0)
  numbers = tokenized_input
  return [fn, numbers]
  

def evaluate_input(input):
  calculation = 0
  fn = input[0]
  numbers = input[1]

  #brute force
  if(len(numbers) > 1):
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    if(fn == '+'):
      calculation = arithmetic.add(num1, num2)
    if(fn == '-'):
      calculation = arithmetic.subtract(num1, num2)
    if(fn == '*'):
      calculation = arithmetic.multiply(num1, num2)
    if(fn == '/'):
      calculation = arithmetic.divide(num1, num2)
    if(fn == '%'):
      calculation = arithmetic.mod(num1, num2)
  else:
    numbers = int(numbers.pop())
    if(fn == '^2'):
      calculation = arithmetic.square(numbers)
    if(fn == '^3'):
      calculation = arithmetic.cube(numbers)
    if(fn == '^'):
      calculation = arithmetic.power(numbers)
  
  return calculation

while(run_calculator == True):
  input = get_input()
  output = evaluate_input(input)
  print output