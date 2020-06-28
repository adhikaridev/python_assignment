# 35.​ Write a Python program to iterate over dictionaries using for loops.

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Original dictionary: ", dict1)

print("Iteration: ")
for key, value in dict1.items():
    print(key, value)
