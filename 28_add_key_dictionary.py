# 28. ​ Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict1 = {}
n = int(input("Enter number of items in the original dictionary: "))
for x in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter corresponding value: "))
    dict1[key] = value
print("Original: ",dict1)
key = int(input("Enter a key to be added: "))
value= int(input("Enter its value: "))
dict1[key] = value
print("After adding: ", dict1)
