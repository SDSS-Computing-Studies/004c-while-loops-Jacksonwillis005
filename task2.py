#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

"""
we are going to be checking the value of the variable "name"
before we have input that creates it, so we should create
a variable with no contents otherwise the conditional statement
might throw an error stating that the variable does not exist

Structure:

create a username and password variable
use while loop to repeat the following block if the password is not correct:
    enter the username
    enter the password
    check to see if the username and password are both correct
        print Access granted if they're both correct
        print Access denied if at least one is wrong


"""


username = ""
password = ""

while username!="admin" or password!="12345":
    username=input("Enter a Username: ")
    password=input("Enter a Password: ")
    username=str(username)
    password=str(password)

    if username=="admin" and password=="12345":
        print("Access granted")
    else:
        print("Access denied")