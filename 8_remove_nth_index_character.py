# 8. ​ Write a Python program to remove the n​th​ index character from a nonempty
# string.

str1 = input("Enter a string: ")
str2 = ""
if str1:
    n = (input("Enter the index of character you want to remove: "))
    if n:
        n = int(n)
        if n < len(str1) and n >= -len(str1):
            str2 = str2 + str1[:n] + str1[n+1:]
            print(str2)
        else:
            print("Index out of range")
    else:
        print("Index not entered")

else:
    print("Empty string")
