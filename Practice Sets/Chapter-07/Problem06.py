# Write a program to calculate the factorial of a given number using for loop

fact = 1
num = int(input("Enter Number: "))
for i in range(1, num+1):
    fact*=i
print(f"Factorial of {num} is {fact}")