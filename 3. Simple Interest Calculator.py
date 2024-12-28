# This is a simple interest calculator program.
# It takes user input for principal amount, rate of interest, and time period.
# It calculates simple interest and compound interest.

def get_input(prompt):
    # this function handles user input

    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Invalid input! Please enter a valid numeric value.")
                continue
            return num
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

def calculator():

    # Main calculator function

    print("This is a simple interest calculator program.")

    print('\nAlthough it is called "simple interest calculator", it also calculates compound interest.')

    p = get_input("\nEnter the principal amount: ")
    r = get_input("Enter the rate of interest: ")
    t = get_input("Enter the time period in years: ")

    si = (p * r * t) / 100
    ci = (p * ((1 + (r / 100)) ** t)) - p

    print(f"\nSimple Interest: {si}")
    print(f"Compound Interest: {ci}")

calculator()