operation = input("Enter the operation you want to perform (+, -, *, /): ")

if operation not in ['+', '-', '*', '/']:
    print("Enter a valid operation nigga!")
else:
    try:
        num1 = float(input("Enter the 1st operand: "))
    except:
        print("You don't know what numbers are? Are you fucking retarded?")
    else:
        try:
            num2 = float(input("Enter the 2nd operand: "))
        except:
            print("You don't know what numbers are? Are you fucking retarded?")
        else:
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
                try:
                    result = num1 / num2
                except:
                    print("If you would have paid attention in class in the 6th grade, you would know that you can't divide by zero, you fucking moron!")
                else:
                    print(f"The quotient of {num1} and {num2} is {result}.")