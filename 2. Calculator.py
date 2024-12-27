def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid Input! Please enter a numeric value.")

def calculator():
    print("Welcome to the calculator program!")
    print("\nAvaiable operations: +, -, *, /")

    operation = input("\nEnter the operation you want to perform (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        print("Invalid Input! Please enter a valid operation: +, -, *, /")
        return

    num1 = get_input("Enter the 1st operand: ")
    num2 = get_input("Enter the 2nd operand: ")

    if operation == '+':
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
    elif operation == '-':
        result = num1 - num2
        print(f"The difference between {num1} and {num2} is {result}.")
    elif operation == '*':
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}.")
    elif operation == '/':
        if num2 == 0:
            print("Division by zero is not possible. Try again next time.")
        else:
            print(f"The quotient of {num1} and {num2} is {result}.")

calculator()