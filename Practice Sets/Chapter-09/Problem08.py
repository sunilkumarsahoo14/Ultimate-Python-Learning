# Write a program to make a copy of a text file “abc. txt”

with open("abc.txt") as f:
    content = f.read()

with open("abc_copy.txt", "w") as f:
    f.write(content)
