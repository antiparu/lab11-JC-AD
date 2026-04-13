import math   #at first,  we import the math library so we can use math.log()

#Josh Carrington as Partner 1
#Alejandro Delgado as Partner 2


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


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)


def mul(a, b):
    return a * b   #we return the product of a and b


def div(a, b):
    #we raise a ZeroDivision error if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")  #this is the error if we cant divide by 0
    return a / b   #otherwise, we return b / a


def exp(a, b):
    return a ** b
