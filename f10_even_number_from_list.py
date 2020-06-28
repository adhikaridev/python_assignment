# 10.​ Write a Python program to print the even numbers from a given list.
# Sample List : ​ [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result ​ : [2, 4, 6, 8]

def even_list(list1):
    list2 = [item for item in list1 if item%2 == 0]
    return list2

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list: ", list1)
print("List with even numbers: ", even_list(list1))
