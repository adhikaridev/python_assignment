# 10. ​ Write a Python program to remove the characters which have odd index
# values of a given string.

str1 = input("Enter a string: ")
str2 = ""

for c in str1[::2]:
    str2 = str2 + c

print(str2)
