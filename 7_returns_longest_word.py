# 7. ​ Write a Python function that takes a list of words and returns the length of the
# longest one.

def longest_length(w_list):
    length = 0
    for w in w_list:
        if length < len(w):
            length = len(w)
    return length


n = int(input("Enter number of words: "))
print("Enter words:")
word_list = []

for i in range(n):
    word = input()
    word_list.append(word)

print("Longest length: ", longest_length(word_list))
