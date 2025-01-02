def get_input():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    return weight, height

def bmi_calculator():
    w, h = get_input()

    bmi = w / (h * h)

    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator!\n")

bmi = bmi_calculator()
category = bmi_category(bmi)

print(f"\nYou BMI is {bmi}.")
print(f"You are {category}.")