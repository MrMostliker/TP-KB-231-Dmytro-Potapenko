# Операції
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

# Головна функція
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
            print("Goodbye!")
            break
        
        # Перевірка вибору операції
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue
            
            match choice:
                case '1':
                    print(f"Result: {add(num1, num2)}")
                case '2':
                    print(f"Result: {subtract(num1, num2)}")
                case '3':
                    print(f"Result: {multiply(num1, num2)}")
                case '4':
                    print(f"Result: {divide(num1, num2)}")
                case '5':
                    print(f"Result: {modulus(num1, num2)}")
                case '6':
                    print(f"Result: {exponent(num1, num2)}")
                case '7':
                    print(f"Result: {floor_division(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")

# Запуск
calculator()
