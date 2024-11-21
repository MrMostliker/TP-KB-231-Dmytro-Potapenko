import logging
from functions import add, subtract, multiply, divide, modulus, exponent, floor_division

class OperationManager:
    def get_numbers(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            logging.warning("Некоректне введення даних користувачем.")
            print("Invalid input! Please enter numerical values.")
            return None, None

    def process_choice(self, choice):
        num1, num2 = self.get_numbers()
        if num1 is None or num2 is None:
            return
        
        operations = {
            '1': ('Addition', add),
            '+': ('Addition', add),
            '2': ('Subtraction', subtract),
            '-': ('Subtraction', subtract),
            '3': ('Multiplication', multiply),
            '*': ('Multiplication', multiply),
            '4': ('Division', divide),
            '/': ('Division', divide),
            '5': ('Modulus', modulus),
            '%': ('Modulus', modulus),
            '6': ('Exponentiation', exponent),
            '**': ('Exponentiation', exponent),
            '7': ('Floor Division', floor_division),
            '//': ('Floor Division', floor_division),
        }
        
        if choice in operations:
            operation_name, func = operations[choice]
            result = func(num1, num2)
            logging.info(f"Операція: {operation_name}, Введені дані: {num1}, {num2}, Результат: {result}")
            print(f"Result: {result}")
        else:
            logging.warning("Користувач обрав некоректну операцію.")
            print("Invalid choice!")
