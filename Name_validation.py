"""This Project is to check Name Validation in the Login

Code created : 12-08-2021
Created By : Harish.v
IDE : PyCharm

# code logic is has follow >>
               Name validation check

>> if user_name is less then 3 char > "Name is very short"
>> else if user_name is more than 60 char > " Name is very long"
>> else user_name is less than 60 char > " Name is validated"

"""

user_name  = str(input("Enter the user_name :"))

if len(user_name) < 3 :
    print("Name is very short")

elif len(user_name) > 60 :
    print(" Name is very long")

else :
    print(" Name is validated")
