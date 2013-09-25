def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def square(num1):
  return multiply(num1, num1)

def cube(num1):
  return multiply(num1, multiply(num1, num1))

def power(num1, num2):
  num = num1
  for i in range(num1-1):
    num = multiply(num, num1)
  return num

def mod(num1, num2):
  div = divide(num1, num2)
  rem = subtract(num1, multiply(div, num2))
  return rem
