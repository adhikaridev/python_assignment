# 12.​ Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

multiply_by_unknown = lambda n: n * 3   # 3 is taken as unknown number here

def my_function(n):
    n = multiply_by_unknown(n)
    return n

n = int(input("Enter a number: "))
result1 = my_function(n)
print("Result: ", result1)
