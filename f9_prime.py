# 9.​ Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.

def prime_check(n):
    a = 1
    for x in range(2, n):
        if n%x == 0:
            a = 0
            break
    if a == 0:
        print("{} is not prime".format(n))
    else:
        print("{} is prime".format(n))

n = int(input("Enter a number: "))
prime_check(n)
