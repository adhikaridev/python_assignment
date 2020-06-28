# 43.​ Write a Python program to remove an item from a tuple.

tup1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print("Original tuple: ", tup1)
str1 = input("Enter the item you want to remove: ")
list1 = list(tup1)
list1.remove(str1)
tup1 = tuple(list1)
print("After removing: ", tup1)
