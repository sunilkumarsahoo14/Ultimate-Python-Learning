# Write a program to find whether a given number is prime or not.

num = int(input("Enter Number: "))

for i in range(2, num):
    if(num%i) == 0:
        print("Number is not prime!")
        break
else:
    print("Number Is Prime.")