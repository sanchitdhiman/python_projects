# This is an age calculator program.
# It takes user input for the birthdate of the user and calculates their age.

from datetime import datetime    # using the datetime module

def get_input():
    # This function inputs the user's date of birth and returns it as a datetime object

    date = input("Enter your birthdate in the format DD/MM/YYYY: ")

    try:
        # extracting day, month, and year separately from the input
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])

        # creating a datetime object and returning it
        return datetime(year, month, day)
    # exception handling
    except ValueError:
        print("Invalid input! Please enter a valid date in the format DD/MM/YYYY.")
        return get_input()  # to take input again

def calculate_age(birthdate):

    # getting today's date
    today = datetime.today()

    # calculating the difference between both dates
    age = today - birthdate
    return age  # in days, hours, minutes, seconds, and microseconds

def calculator():
    # main calculator program

    print("Welcome to the Age Calculator!")
    print("\nThis program calculates your age based on your birthdate.")

    birthdate = get_input()
    age = calculate_age(birthdate)

    print(f"\nYour age is {age.days // 365} years.")    # extracting only days from the difference then converting into years.

    print("\nThank you for using the Age Calculator!")

calculator()
