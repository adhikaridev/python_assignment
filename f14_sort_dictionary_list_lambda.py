# 14.​ Write a Python program to sort a list of dictionaries using Lambda.


get_first_value = lambda data: data.get('s')      #sorting according to the first value of dictionaries

list1 = [{'s': 2, 'a': 1}, {'s': 5}, {'s': 3, 'd': 4}, {'s': 0}, {'s': 1}, {'s': 4}]
print("Original list: ", list1)
list1.sort(key=get_first_value)
print("Sorted list according to the first value of dictionaries: ", list1)
