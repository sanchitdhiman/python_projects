# This is a temperature converter program.
# It takes user input for temperature value and its current scale.
# It calculates the temperature value in other two scales and prints the converted values.

def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9 / 5) - 459.67

def temperature_converter():

    # the main calculator

    print("This is a temperature converter program.")

    print("\nAvailable scales: Celsius (C), Fahrenheit (F), Kelvin (K)")

    scale = input("\nEnter the scale you want to convert from (C, F, or K): ").upper()

    if scale not in ['C', 'F', 'K']:
        print("Invalid scale! Please enter a valid scale: C, F, or K.")
        return

    temp = get_input("Enter the temperature value: ")

    if scale == 'C':
        print(f"\nTemperature in Celsius: {temp}")
        print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temp)}")
        print(f"Temperature in Kelvin: {celsius_to_kelvin(temp)}")
    elif scale == 'F':
        print(f"\nTemperature in Fahrenheit: {temp}")
        print(f"Temperature in Celsius: {fahrenheit_to_celsius(temp)}")
        print(f"Temperature in Kelvin: {fahrenheit_to_kelvin(temp)}")
    elif scale == 'K':
        print(f"\nTemperature in Kelvin: {temp}")
        print(f"Temperature in Celsius: {kelvin_to_celsius(temp)}")
        print(f"Temperature in Fahrenheit: {kelvin_to_fahrenheit(temp)}")

    print("\nThank you for using the temperature converter program!")

temperature_converter()