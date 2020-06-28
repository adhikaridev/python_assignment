# 18.​ Write a Python program to check whether a given string is number or not
# using Lambda.

check_num = lambda str1: True if str1.isnumeric() else False

str1 = input("Enter a string: ")
b = check_num(str1)
if b:
    print("{} is a number.".format(str1))
else:
    print("{} is not a number.".format(str1))
