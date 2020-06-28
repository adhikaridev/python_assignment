# 4.​ Write a Python program to reverse a string.
# Sample String ​ : "1234abcd"
# Expected Output ​ : "dcba4321"

def reverse(str1):
    list1 = list(str1)
    list1.reverse()
    list1 = "".join(list1)
    return list1

str1 = input("Enter a string: ")
print("Original string: ", str1)
print("Reversed string: ", reverse(str1))
