# Write a program to find whether a given username contains less than 10 characters or not.

user_name = input("Enter Username: ")

if(len(user_name) < 10):
    print("User Name Is Less Than 10 Characters!")
else:
    print("All Good, User Name Contains More Than 10 Characters.")