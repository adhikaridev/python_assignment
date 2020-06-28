# 19.​ Write a Python program to get the smallest number from a list.

n = int(input("Enter number of items in a list: "))
print("Enter integer items: ")
list1 = []

for x in range(n):
    list1.append(int(input()))
print(list1)
print("Smallest item: ", min(list1))
