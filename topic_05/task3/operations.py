from functions import add, subtract, multiply, divide, modulus, exponent, floor_division

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return None, None

def perform_operation(choice, num1, num2):
    match choice:
        case '1' | '+':
            return add(num1, num2)
        case '2' | '-':
            return subtract(num1, num2)
        case '3' | '*':
            return multiply(num1, num2)
        case '4' | '/':
            return divide(num1, num2)
        case '5' | '%':
            return modulus(num1, num2)
        case '6' | '**':
            return exponent(num1, num2)
        case '7' | '//':
            return floor_division(num1, num2)
        case _:
            return "Invalid choice!"
