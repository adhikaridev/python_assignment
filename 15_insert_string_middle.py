# 15.​ Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_middle(str1, str2):
    mid_length = int(len(str1)/2);
    return str1[:mid_length] + str2 + str1[mid_length:]

str1 = input("Enter a string with even number of characters in which you want to insert: ")
str2 = input("Enter a string which you want to insert: ")

print("New string: ", insert_middle(str1, str2))
