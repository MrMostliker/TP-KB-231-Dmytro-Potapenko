def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def floor_division(a, b):
    if b != 0:
        return a // b
    else:
        return "Division by zero is not allowed!"