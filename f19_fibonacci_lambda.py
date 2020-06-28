# 19.​ Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce

add_prev_two = lambda x, _: x + [x[-1] + x[-2]]
fib = lambda n: reduce(add_prev_two, range(n - 2), [0, 1])

n = int(input("Enter the number of items in the series: "))
print("Fibonacci series: ", fib(n))
