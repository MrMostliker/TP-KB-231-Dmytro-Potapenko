# Operator priority
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

# Is operator?
def is_operator(c):
    return c in '+-*/^'

# Infix to RPN
def infix_to_postfix(expression):
    output = []
    stack = []

    for char in expression:
        if char.isdigit() or char.isalpha():  # Operand (Number or variable)
            output.append(char)
        elif char == '(':  
            stack.append(char)
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Del '('
        elif is_operator(char):  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    # Add remaining operators in stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Calculating
def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():  # Number
            stack.append(int(char))
        elif is_operator(char):  # Operator
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)

    return stack[0] 

#Start
if __name__ == "__main__":
    infix_expr = input("Введіть математичний вираз: ").replace(' ', '')
    postfix_expr = infix_to_postfix(infix_expr)
    print(f"Зворотний польський запис: {postfix_expr}")
    result = evaluate_postfix(postfix_expr)
    print(f"Результат обчислення: {result}")
