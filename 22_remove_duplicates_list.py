# 22. ​ Write a Python program to remove duplicates from a list.

n = int(input("Enter number of items in a list: "))
print("Enter items: ")
list1 = []
list2 = []
for x in range(n):
    item = input()
    list1.append(item)
    if item not in list2:
        list2.append(item)
print("Original list: ", list1)
print("List after removing duplicates: ", list2)
