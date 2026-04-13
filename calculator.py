import math   #at first,  we import the math library so we can use math.log()

def add(a, b):
    return a + b   #we return the sum of a and b

# First example
def square_root(a):
    if a < 0:
        raise ValueError("Value cannot be negative")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a,b):
    return a - b

def logarithm(a,b):
    try:
        result = math.log(a, b)
    except ValueError:
        print("Invalid input for logarithm.")
        

def mul(a, b):
    return a * b   #we return the product of a and b

def div(a, b):
    #we raise a ZeroDivision error if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")  #this is the error if we cant divide by 0
    return b / a   #otherwise, we return b / a



def exp(a, b):
    return a ** b
