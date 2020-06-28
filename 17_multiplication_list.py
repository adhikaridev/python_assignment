# 17.​ Write a Python program to multiplies all the items in a list.

n = int(input("Enter number of items in a list: "))
print("Enter integer items: ")
list1 = []
prod = 1
for x in range(n):
    list1.append(int(input()))
print(list1)
for item in list1:
    prod = prod * item
print("Product: ", prod)
