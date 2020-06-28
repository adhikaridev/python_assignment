# 6.​ Write a Python function to check whether a number is in a given range.

def check_in_range(n):
    if n in range(5, 15):
        return True
    else:
        return False

print("Range: 5 - 15")
n = int(input("Enter a number: "))
b = check_in_range(n)
if b:
    print("The number is in the range.")
else:
    print("The number is not in the range.")
