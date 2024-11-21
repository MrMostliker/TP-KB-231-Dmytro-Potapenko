import logging
from operations import OperationManager

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class Calculator:
    def __init__(self):
        self.operations = OperationManager()
        logging.info("Калькулятор ініціалізовано.")

    def display_menu(self):
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Floor Division (//)")
        print("Type 'exit' to quit.")

    def run(self):
        print("Welcome to the calculator!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == 'exit':
                logging.info("Користувач завершив роботу.")
                print("Goodbye!")
                break
            self.operations.process_choice(choice)
