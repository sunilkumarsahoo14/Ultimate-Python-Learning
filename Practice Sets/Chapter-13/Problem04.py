# Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 3, 5,6,67867, 344, 2]

f = list(filter(divisible5, a))
print(f)