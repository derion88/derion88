import math

# This program will allow a user to calculate investment interest rates and home loan interest rates
# Collecting user data
choice = input('''Please choose either \'investment' or \'bond' from the menu below to proceed: \n 
investment           - to calculate the amount of interest you'll earn in interest
bond                 - to calculate the amount you'll have to pay on a home loan
\nEnter your choice here: ''')


choice = choice.lower()
if not choice == "bond" and not choice == "investment":
    print("Please enter either: \"investment\" or \"bond.\" ")

if choice == "investment":
    P = float(input("Please enter the amount you would like to deposit: R"))
    r = float(input("Please enter the interest rate here: "))
    t = int(input("For how many years would you like to invest this amount? "))
    interest = input("Please indicate if you would like \"simple\" or \"compound\" interest on this amount: ")

    # Calculating total simple interest
    interest = interest.lower()
    if interest == "simple":
        r = r/100
        A = round(P*(1 + r * t), 2)
        total_inter = round((P * r * t), 2)
        print(f'\nFor this investment you will make R{total_inter} in simple interest and a total of R{A}.')

    # Calculating total compound interest
    if interest == "compound":
        r = r/100
        A = round(P * math.pow((1 + r), t), 2)
        comp_amount = round((A - P), 2)
        print(f'\nFor this investment you will make R{comp_amount} in compound interest and total amount of R{A}.')


if choice == "bond":
    P = float(input("\nPlease enter the present value of the house: R"))
    i = float(input("What is the current interest rate of the house: "))
    n = int(input("Please enter the number of months in which you plan to repay the bond: "))

# Calculating the monthly repayment amount for a bond
# I looked up the following formula on the website indicated below
# https://medium.com/swlh/simple-mortgage-calculator-with-python-and-excel-b98dede36720
# Formula in example didn't seem to work, compared to other calculators on the web

    i = (i/100)/12
    amount_1 = i * ((1 + i)**n)
    amount_2 = (1 + i)**n-1
    x = round(P*(amount_1/amount_2), 2)
    print(f"\nFor this bond your monthly repayment will be R{x}.")

print("\nThank you :)")
