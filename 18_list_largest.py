# 18.​ Write a Python program to get the largest number from a list.

n = int(input("Enter number of items in a list: "))
print("Enter integer items: ")
list1 = []

for x in range(n):
    list1.append(int(input()))
print(list1)
print("Largest item: ", max(list1))
