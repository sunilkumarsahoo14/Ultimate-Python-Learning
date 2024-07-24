#  Write a program to detect double space in a string.

str = input("Enter String: ")

# String find function is used - it return (-1) if not found &
# if found the character then it return the index position
print(str.find("  "))