# 23. ​ Write a Python program to check a list is empty or not.
# Enter a list: []
# List is empty
# ['']
#
# Enter a list: [a]
# List is not empty
# ['a']
#
# Enter a list: [1, 2, 3]
# List is not empty
# ['1', '2', '3']




str1 = input("Enter a list: ")
list1 = []
list1 = str1[1:-1].split(", ")

if list1[0] == "":
    print("List is empty")
else:
    print("List is not empty")
print(list1)
