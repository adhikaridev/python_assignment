# 20.​ Write a Python program to find intersection of two given arrays using
# Lambda.

is_common = lambda x: True if x in array1 else False

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
array2 = [2, 3, 5, 7, 11, 100]

intersection_array = list(filter(is_common, array2))
print("Array 1: ", array1)
print("Array 2: ", array2)
print("Intersection array: ", intersection_array)
