# 15.​ Write a Python program to filter a list of integers using Lambda.

get_positive = lambda x: x > 0  #returns true or false
get_negative = lambda x: x < 0  #returns true or false

list1 = [2, -1, 3, -2, 4, -3, -5, 6, 9, -4, -7]
print("Original list: ", list1)
result1 = filter(get_positive, list1)
result2 = filter(get_negative, list1)

print("Positive integer list: ", list(result1))
print("Negative integer list: ", list(result2))
