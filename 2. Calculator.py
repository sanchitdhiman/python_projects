# This is a simple calculator program.
# It performs four basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).


def get_input(prompt):
    # function to get a numeric input from the user

    while True:
        # handling invalid input exceptions
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input! Please enter a numeric value.")

def calculator():

    # The calculator program

    print("Welcome to the calculator program!")
    print("\nAvailable operations: +, -, *, /")

    # get the operation from the user
    operation = input("\nEnter the operation you want to perform (+, -, *, /): ")

    # check if the operation is valid
    if operation not in ['+', '-', '*', '/']:
        print("Invalid Input! Please enter a valid operation: +, -, *, /")
        return

    # receiving numerical inputs from the user
    num1 = get_input("Enter the 1st operand: ")
    num2 = get_input("Enter the 2nd operand: ")

    # performing the calculation based on the operation
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
        # handling division by zero exception
        if num2 == 0:
            print("Division by zero is not possible. Try again next time.")
        else:
            result = num1 / num2
            print(f"The quotient of {num1} and {num2} is {result}.")

    print("\nThank you for using the calculator program!")


# calling the calculator function
calculator()