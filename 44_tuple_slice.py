# 44.​ Write a Python program to slice a tuple.

tup1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print("Original tuple: ", tup1)
a = int(input("Enter start index (included): "))
z = int(input("Enter stop index (excluded): "))
i = int(input("Enter step size: "))
print("Tuple after slicing: ", tup1[a:z:i])
