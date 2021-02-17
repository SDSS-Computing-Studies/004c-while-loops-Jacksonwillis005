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

username=input("Enter a Username: ")
password=input("Enter a Password: ")
username=str(username)
password=str(password)

if username=="admin" and password=="12345":
    print("Access granted")
else:
    print("Access denied")