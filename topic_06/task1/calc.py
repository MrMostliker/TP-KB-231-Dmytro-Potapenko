import logging
from operations import get_numbers, perform_operation

logging.basicConfig(
    filename="calculator.log",  
    level=logging.INFO,         
    format="%(asctime)s - %(levelname)s - %(message)s",  
)

def calculator():
    print("Welcome to the calculator!")
    print("Type 'exit' at any time to quit.")
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Floor Division (//)")
        
        choice = input("Enter the number of the operation (1-7) or 'exit' to quit: ").strip().lower()
        
        if choice == 'exit':
            logging.info("Користувач завершив роботу.")
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '+', '-', '*', '/', '%', '**', '//']:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue
            
            result = perform_operation(choice, num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

# Start the calculator
if __name__ == "__main__":
    logging.info("Запуск програми калькулятор.")
    calculator()
    logging.info("Програма завершена.")
