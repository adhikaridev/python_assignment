# 2.​ Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String


str1 = input("Enter a string: ")
# str1 = "Python"
str2 = ""

if len(str1) >= 2:
    str2 = str1[:2] + str1[-2:]
else:
    str2 = "Empty String"


print(str2)
