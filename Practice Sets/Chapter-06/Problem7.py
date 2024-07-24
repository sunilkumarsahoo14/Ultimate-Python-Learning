# Write a program to find out whether a given post is talking about “Harry” or not.

post = "Hello, I am Sunil and I am learning python from harry bhai. The course is really awesome!" # you can also take user inputs

if("Harry".lower() in post.lower()):
    print("This post is talking about harry.")
else:
    print("This post is not talking about harry.")