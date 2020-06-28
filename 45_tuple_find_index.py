# 45.​ Write a Python program to find the index of an item of a tuple.

tup1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print("Original tuple: ", tup1)
str1 = input("Enter the item whose index you want: ")
if str1 in tup1:
    print("Index: ", tup1.index(str1))
else:
    print("Item not found.")
