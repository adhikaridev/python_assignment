# 16.​ Write a Python program to square and cube every number in a given list of
# integers using Lambda.

squares = lambda x: x*x
cubes = lambda x: x*x*x

list1 = [1, 2, 3, 4, 5]
list2 = list(map(squares, list1))
list3 = list(map(cubes, list1))
print("Original list: ", list1)
print("Squares list: ", list2)
print("Cubes list: ", list3)
