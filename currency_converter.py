print("Welcome to the ultimate currency converter app")

amount = input("Please type a amount to be converted: ")

if amount.isdigit():
    amount = float(amount)
else:
    print("Type a valid amount: ")

currencies = ['1. INR', '2. USD', '3. EUR', '4. CAD', '5. AUD']

for i in currencies:
    print(i)

from_currency = int(input("Select the currency of the amount you want to convert from the above list(choose number): "))

to_currency = int(input("Select the currency to which you want to convert from the above list(choose number): "))

# US dollars to other currencies
if from_currency == 2: 
    if to_currency == 1:
        conversion = amount * 79.90
        print("{} USD = {} INR".format(amount, conversion))
    elif to_currency == 3:
        conversion = amount * 0.99
        print("{} USD = {} EUR".format(amount, conversion))
    elif to_currency == 4:
        conversion = amount * 1.30
        print("{} USD = {} CAD".format(amount, conversion))
    else:
        conversion = amount * 1.47
        print("{} USD = {} AUD".format(amount, conversion))

# Indian rupees to other currencies
if from_currency == 1: 
    if to_currency == 2:
        conversion = amount * 0.013
        print("{} INR = {} USD".format(amount, conversion))
    elif to_currency == 3:
        conversion = amount * 0.012
        print("{} INR = {} EUR".format(amount, conversion))
    elif to_currency == 4:
        conversion = amount * 0.016
        print("{} INR = {} CAD".format(amount, conversion))
    else:
        conversion = amount * 0.018
        print("{} INR = {} AUD".format(amount, conversion))