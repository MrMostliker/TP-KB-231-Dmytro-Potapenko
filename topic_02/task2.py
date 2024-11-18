# Operation func's
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

# Main function
def calculator():
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")

    choice = input("Enter the number of the operation (1-7): ")

    # Validate the choice of operation
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numerical values!")
            return
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {modulus(num1, num2)}")
        elif choice == '6':
            print(f"Result: {exponent(num1, num2)}")
        elif choice == '7':
            print(f"Result: {floor_division(num1, num2)}")
    else:
        print("Invalid operation choice!")

# Start
calculator()
