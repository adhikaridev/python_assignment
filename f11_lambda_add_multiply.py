# 11.​ Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

addition = lambda n: n + 15

mul = lambda x, y: x * y

n = int(input("Enter a number: "))
result1 = addition(n)
print("Result of addition: ", result1)

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
result2 = mul(x, y)
print("Result of multiplication: ", result2)
