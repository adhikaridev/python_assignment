# 6.​ Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

str1 = input("Enter a string: ")
str2 = ""

if "not" in str1 and "poor" in str1 and str1.find("not") < str1.find("poor"):
    str2 = str2 + str1[:str1.find("not")] + "good" + str1[str1.find("poor")+4:]
else:
    str2 = str1

print(str2)
