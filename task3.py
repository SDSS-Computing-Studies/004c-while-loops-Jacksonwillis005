#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
import math
num=1

while num % 2 != 0:
    num = float(input("Enter a number: "))
    if (num % 2) == 0:
        print("That is an even integer".format(num))
    else:
        print("That is not an even integer".format(num))