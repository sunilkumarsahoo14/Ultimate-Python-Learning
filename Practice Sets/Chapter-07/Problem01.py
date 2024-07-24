# Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter number: "))

i = 1
while(i <= 10):
    print(f"{num} X {i} = {num*i}")
    i = i+1