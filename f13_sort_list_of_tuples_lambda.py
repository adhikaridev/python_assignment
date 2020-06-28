# 13.​ Write a Python program to sort a list of tuples using Lambda.

get_second_item = lambda data: data[1]      #sorting according to the second item of tuple

list1 = [(5, 3), (2, 1), (3, 1), (2, 0), (4, 5), (1, 1)]
print("Original list: ", list1)
list1.sort(key=get_second_item)
print("Sorted list according to the second item of tuple: ", list1)
