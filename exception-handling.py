#2 types of errors: syntax errors & logic errors

#Syntax errors - errors in the structure of the statement or expression
#Python Interpreter can't complete the processing of the instruction

#Logic errors - error in the underlying algorithm
#Can lbe due to division by zero or trying to access an item in a list where the index of the item is outside the bounds of the list
#Leads to runtime error as it causes program to terminate - called EXCEPTIONS

#An exception is *raised* - which can be *handled*

import math

n = input("Enter a number")
try: 
    print(math.sqrt(int(n)))
except: 
    if n is int:
        print("Taking the absolute value instead")
        print(math.sqrt(abs(int(n))))
    else:
        print("Enter a number not a character")

