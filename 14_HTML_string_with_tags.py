# 14.​ Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


def add_tags(tag, word):
    return "<{}>{}</{}>".format(tag, word, tag)

word = input("Enter word/words: ")
tag = input("Enter tag: ")
html_string = add_tags(tag, word)
print("HTML string:", html_string)
