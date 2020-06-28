# 8.​ Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : ​ [1,2,3,3,3,3,4,5]
# Unique List : ​ [1, 2, 3, 4, 5]

def list_unique(list1):
    set1 = set(list1)
    list1 = list(set1)
    return list1

list1 = [1,2,3,3,3,3,4,5]
print("Original list: ", list1)
print("List with unique elements: ", list_unique(list1))
