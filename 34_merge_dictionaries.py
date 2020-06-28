# 34.​ Write a Python script to merge two Python dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 1, 'd': 4}
print("Dictionary 1: ", dict1)
print("Dictionary 2: ", dict2)
dict1.update(dict2)
print(dict1)
