operation = input("Enter the operation you want to perform (+, -, *, /): ")

if operation == '+':
    num1 = float(input("Enter the 1st operand: "))
    num2 = float(input("Enter the 2nd operand: "))

    result = num1 + num2

    print(f"The sum of {num1} and {num2} is {result}.")
elif operation == '-':
    num1 = float(input("Enter the 1st operand: "))
    num2 = float(input("Enter the 2nd operand: "))

    result = num1 - num2

    print(f"The difference between {num1} and {num2} is {result}.")
elif operation == '*':
    num1 = float(input("Enter the 1st operand: "))
    num2 = float(input("Enter the 2nd operand: "))

    result = num1 * num2

    print(f"The product of {num1} and {num2} is {result}.")
elif operation == '/':
    num1 = float(input("Enter the 1st operand: "))
    num2 = float(input("Enter the 2nd operand: "))

    result = num1 / num2

    print(f"The quotient of {num1} and {num2} is {result}.")
else:
    print("Enter a valid operation nigga!")