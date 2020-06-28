# 9. ​ Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.



str1 = input("Enter a string: ")
if str1:
    str2 = str1[-1] + str1[1:-1] + str1[0]
    print(str2)
else:
    print("String is empty")
