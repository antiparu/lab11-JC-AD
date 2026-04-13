import math   #at first,  we import the math library so we can use math.log()

def add(a, b):
    return a + b   #we return the sum of a and b

def sub(a, b):
    return a - b   #we return the result of the subtraction b from a

def mul(a, b):
    return a * b   #we return the product of a and b

def div(a, b):
    #we raise a ZeroDivision error if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")  #this is the error if we cant divide by 0
    return b / a   #otherwise, we return b / a

def log(a, b):
    # computing log of b with base using math.log(b,a)

    #we must raise ValueError for invalid inputs

    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)   #we compute log_a(b)

def exp(a, b):
    return a ** b
