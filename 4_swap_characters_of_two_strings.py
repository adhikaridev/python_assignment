# 4.​ Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

str3 = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

print(str3)
