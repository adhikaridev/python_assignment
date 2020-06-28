# 3.​ Write a Python function to multiply all the numbers in a list.
# Sample List : ​ (8, 2, 3, -1, 7)
# Expected Output ​ : -336

def prod(list1):
    p = 1
    for item in list1:
        p = p * item
    return p

list1 = [8, 2, 3, -1, 7]
print("Original list: ", list1)
print("Product: ", prod(list1))
