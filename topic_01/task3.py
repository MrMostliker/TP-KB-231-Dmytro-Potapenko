def get_coefficients():
    print("Enter your coefficients (ax^2 + bx + c):")
    a = float(input('Enter your a: '))
    b = float(input('Enter your b: '))
    c = float(input('Enter your c: '))
    return a, b, c

def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

a, b, c = get_coefficients()
print("The discriminant is:", discriminant(a, b, c))
