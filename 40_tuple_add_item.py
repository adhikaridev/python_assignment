# 40.​ Write a Python program to add an item in a tuple.

tup1 = ('a', 'b', 'c')
print("Original tuple: ", tup1)
str1 = input("Enter an item to be added: ")
tup2 = (str1,)
print("After adding item: ", tup1 + tup2)
