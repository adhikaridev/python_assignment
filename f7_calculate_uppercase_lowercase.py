# 7.​ Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String ​ : 'The quick Brow Fox'
# Expected Output : ​
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def calculate_upper_lower(str1):
    upper_count = 0
    lower_count = 0
    for c in str1:
        if c.isupper():
            upper_count += 1
        if c.islower():
            lower_count += 1
    print("No. of uppercase characters: ", upper_count)
    print("No. of lowercase characters: ", lower_count)

str1 = input("Enter a string: ")
calculate_upper_lower(str1)
