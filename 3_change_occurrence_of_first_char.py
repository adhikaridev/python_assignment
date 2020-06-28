# 3. ​ Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

str1 = input("Enter a string: ")
# str1 = "characteristic"
str2 = str1[0]

for s in str1[1:]:
    if s == str1[0]:
        str2 = str2 + "$"
    else:
        str2 = str2 + s

print(str2)
