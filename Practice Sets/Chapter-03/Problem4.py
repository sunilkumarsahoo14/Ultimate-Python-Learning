# Replace the double space from problem 3 with single spaces.

str = input("Enter String: ")

# String find function is used - it return (-1) if not found &
# if found the character then it return the index position
print(str.find("  "))

# Replace the double space by single space
# String are immutable
modify_str = str.replace("  ", " ")

# Print Result String
print("Final String Is:", modify_str)