# This program will calculate a user's BMI

# Collecting user data
print("\nHi, if you would like to know your BMI, please answer the questions below.")
name = input("\nPlease enter your name here: ")
age = int(input("Please input your age here: "))
weight = int(input("Please insert your weight in kilograms: "))
height = float(input("PLease enter your height in meters: "))

# Calculating user's BMI
bmi = round(weight/(height*height), 2)

# Determining if user is obese, overweight, normal weight or under weight
# Then printing result
if bmi >= 30:
    result = "obese"
elif bmi >= 25:
    result = "overweight"
elif bmi >= 18:
    result = "normal weight"
else:
    result = "under weight"
print(f'''\nHi {name}, at age {age}, your BMI is {bmi}.
This means you are {result}.

Thank you :) ''')
