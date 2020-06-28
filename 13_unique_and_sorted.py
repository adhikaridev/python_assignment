# 13. ​ Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

str1 = input("Enter comma separated sequence of words: ")

list1 = str1.split(", ")        #splitting the string into list items on the basis of comma
set1 = set(list1)               #set used to get unique elements
set1 = sorted(set1)             #sorting the set

str2 = ""

for member in set1[:-1:1]:      #for converting set back to the string
    str2 += member + ", "
str2 += set1[-1]
print(str2)
