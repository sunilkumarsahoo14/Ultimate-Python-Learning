# Write a python program to print the contents of a directory using the os module. Search online for the function which does that. & Label the program written in problem 4 with comments. 

import os

# Specify the directory path
directory_path = '/'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)