# 1.​ Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str1 = input("Enter a string: ")

my_dict = {}


for s in str1:
    count = 0
    for t in str1:
        if s == t:
            count += 1
    my_dict[s] = count

a = dict(sorted(my_dict.items(), key = lambda x: x[1], reverse = True))

print(a)
