# 11. ​ Write a Python program to count the occurrences of each word in a given
# sentence.

str1 = input("Enter a sentence: ")
my_dict = {}

if str1:
    if str1[-1] == ".":
        str1 = str1.replace(".", "")   #removing fullstop from the original sentence

    list1 = str1.split()        #converting the given sentence into a list of words

    for s in list1:
        count = 0
        for t in list1:
            if s == t:
                count += 1
        my_dict[s] = count      #dictionary takes only unique keys

    print(my_dict)
else:
    print("Empty string")
