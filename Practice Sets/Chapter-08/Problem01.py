# Write a program using functions to find greatest of three numbers.

# Function to find greatest number
def greatest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

n1 = int(input("Enter Number: "))
n2 = int(input("Enter Number: "))
n3 = int(input("Enter Number: "))

print("Greatest Number Is:", greatest(n1, n2, n3))