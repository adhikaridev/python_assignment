# 17.​ Write a Python program to find if a given string starts with a given character
# using Lambda.

starts = lambda str1, ch: True if str1[0] == ch else False

str1 = input("Enter a string: ")
ch = input("Enter a character: ")
s = starts(str1, ch)
if s:
    print("{} starts with character {}".format(str1, ch))
else:
    print("{} does not start with character {}".format(str1, ch))
