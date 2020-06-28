# 27.​ Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

str1 = input("Enter a list of integers: ")
str2 = input("Enter another list of integers: ")
# str1 = "[1, 3, 5, 7, 9, 10]"
# str2 = "[2, 4, 6, 8]"

list1 = str1[1:-1].split(", ")
list2 = str2[1:-1].split(", ")
list1 = [int(item) for item in list1]
list2 = [int(item) for item in list2]
list1.pop(-1)
list1.extend(list2)
print("Output: ", list1)
