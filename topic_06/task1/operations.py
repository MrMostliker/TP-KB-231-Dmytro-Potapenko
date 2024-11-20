import logging
from functions import add, subtract, multiply, divide, modulus, exponent, floor_division

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        logging.warning("Некоректне введення даних користувачем.")
        print("Invalid input! Please enter numerical values.")
        return None, None

def perform_operation(choice, num1, num2):
    result = None
    operation = ""

    match choice:
        case '1' | '+':
            result = add(num1, num2)
            operation = "Addition"
        case '2' | '-':
            result = subtract(num1, num2)
            operation = "Subtraction"
        case '3' | '*':
            result = multiply(num1, num2)
            operation = "Multiplication"
        case '4' | '/':
            result = divide(num1, num2)
            operation = "Division"
        case '5' | '%':
            result = modulus(num1, num2)
            operation = "Modulus"
        case '6' | '**':
            result = exponent(num1, num2)
            operation = "Exponentiation"
        case '7' | '//':
            result = floor_division(num1, num2)
            operation = "Floor Division"
        case _:
            logging.warning("Користувач обрав некоректну операцію.")
            return "Invalid choice!"
    
 
    if result is not None:
        logging.info(f"Операція: {operation}, Введені дані: {num1}, {num2}, Результат: {result}")
    
    return result
