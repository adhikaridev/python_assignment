# 5.​ Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a non-negative integer: "))
print("Factorial: ", fact(n))
