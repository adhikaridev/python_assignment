# 20.​ Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

n = int(input("Enter number of items in a list: "))
print("Enter items: ")
list1 = []
count = 0

for x in range(n):
    list1.append(input())
print(list1)

for item in list1:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1

print("Count: ",count)
