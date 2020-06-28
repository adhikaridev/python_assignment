# 24. ​ Write a Python program to clone or copy a list.

n = int(input("Enter number of items in a list: "))
print("Enter items: ")
list1 = []

for x in range(n):
    list1.append(input())
print("Original", list1)

list2 = list1.copy()
print("Copied: ", list2)
