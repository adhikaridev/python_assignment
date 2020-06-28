# 38.​ Write a Python program to remove a key from a dictionary.

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Original dictionary: ", dict1)
key = input("Enter the key to be removed: ")
dict1.pop(key)
print("Dictionary after removing the key: ", dict1)
