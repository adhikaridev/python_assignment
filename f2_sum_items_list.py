# 2.​ Write a Python function to sum all the numbers in a list.
# Sample List : ​ (8, 2, 3, 0, 7)
# Expected Output ​ : 20

def sum(list1):
    s = 0
    for item in list1:
        s = s + item
    return s

list1 = [1, 2, 3, 4, 5]
print("Original list: ", list1)
print("Sum: ", sum(list1))
