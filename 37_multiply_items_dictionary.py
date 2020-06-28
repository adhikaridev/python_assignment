# 37.​ Write a Python program to multiply all the items in a dictionary.

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Dictionary: ", dict1)
prod = 1
for value in dict1.values():
    prod *= value
print("Product: ", prod)
