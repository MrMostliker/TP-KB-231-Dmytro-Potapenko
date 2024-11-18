import math

def get_coefficients():                                          #input func
    print("Enter your coefficients (ax^2 + bx + c):")
    a = float(input('Enter your a: '))
    b = float(input('Enter your b: '))
    c = float(input('Enter your c: '))
    return a, b, c

def discriminant(a, b, c):                                       #disc calc func
    return b**2 - 4*a*c

def find_roots(a, b, c):                                         #root calc func
    D = discriminant(a, b, c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Two real roots: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"One real root: x = {x}"
    else:
        return "No real roots exist."

a, b, c = get_coefficients()

if a == 0:                                                       #is possible check
    print("This is not a quadratic equation (a cannot be 0).")
else:
    roots = find_roots(a, b, c)
    print("The roots are:", roots)
