# 25.​ Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

str1 = input("Enter a list of dictionaries: ")
list1 = str1[1:-1].split("},")
list2 = [item + "}" for item in list1[:-1]]
list2.append(list1[-1])
a = True
for element in list2:
    if element != "{}":
        a = False
        break;
print(a)
