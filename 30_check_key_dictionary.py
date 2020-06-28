# 30.​ Write a Python script to check whether a given key already exists in a
# dictionary.

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Original dictionary: ", dict1)
key = input("Enter a key: ")

if key in dict1:
    print("Key already exists.")
else:
    print("Key does not exist already.")
