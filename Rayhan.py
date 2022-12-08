'''
a)You have deposited 20,000 BDT in the bank for a compound interest of 5% per year. This means, that after one year your
balance will be your principal + profit. For the next year (the principal + profit)  will be counted as your new principal
and profit will be calculated on your new principal. And this will go on. What will be your money after 4 years?
[Don’t use the formula C=P(1+r/100)n] [Use  in-Place operator]
'''

a = 20000
a += a*0.05
a += a*0.05
a += a*0.05
a += a*0.05
print("Balance after 4 years=", a)

'''
b)Take all the following inputs of a user: Name, Birth year, Nationality, University/College Name, Living Country, Male/Female, 
and Mobile number (11 digits).
DO NOT USE ANY IF ELSE or Advance CODE
Then, give an output of his/her profile like the following output 👇
Name: Inputted Name here
Age: *** years
Nationality: *** (UPPER CASE)
University/College: ****
Current Location: The inputted living country name
Mobile Number: +8801**********
Gender: True (if male), False (if female)
'''
name = input("Input your name:")
age = int(input("Input your age:"))
nationality = input("Input your Nationality:")
uni = input("Input you University/College:")
loc = input("Input your Living Country:")
num = input("Input your phone number (11 Digit): +88")
gender = input("Input your gender: male or female:").upper()
print("Name:", name)
print("Age:", age, "Years")
print("Nationality:", nationality.upper())
print("University/College:", uni)
print("Current Location:", loc)
print("Mobile Number: +88" + num[0:11])
print("Gender:", "MALE" == gender)
