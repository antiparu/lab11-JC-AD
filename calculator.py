import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError("Value cannot be negative")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return a + b
def subtract(a,b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Divide by zero error")
def logarithm(a,b):
    try:
        result = math.log(a, b)
    except ValueError:
        print("Invalid input for logarithm.")
def exponent(a,b):
    return a ** b

