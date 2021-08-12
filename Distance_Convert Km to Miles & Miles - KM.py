"""
This Project is for Distance Converter KM to Miles & Miles to Km

Code created on : 12-08-2021
code By : Harish.v
IDE : PyCharm

Logic is has followed

>> if Distance Travelled in KM i.e 10Km then converted to Miles
Distance/1.609 formula (for an approximate result, divide the length value by 1.609)

>> elif  Distance Travelled in Miles i.e 10 Miles then converted to KM
Distance * 1.609 formula ( for an approximate result, multiply the length value by 1.609)

------------------------------------------------------------------------------------------------
"""

Distance = int(input("Enter the distance Travelled : "))
unit = input("Input type i.e K for Km  or M for Miles : ")

if unit.upper() == "K":
    converted = Distance/1.609
    print(f"You have covered {converted} Miles")

elif unit.upper() == "M":
    converted = Distance * 1.609
    print(f"you have covered {converted} Km")

else:
    print("Wrong input")
