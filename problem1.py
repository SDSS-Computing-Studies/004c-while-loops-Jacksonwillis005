##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""



username = ""
password = ""

while username!="admin" or password!="12345":
    username=input("enter the username: ").strip()
    password=input("enter the password: ").strip()
    username=str(username)
    password=str(password)

    if username=="admin" and password=="12345":
        print("Access granted")
    else:
        print("Access denied")