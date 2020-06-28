# 26.​ Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

str1 = input("Enter a list: ")
str2 = input("Enter a string to be inserted: ")

list1 = str1[1:-1].split(",")
list1 = [str2 + item for item in list1]
print(list1)
