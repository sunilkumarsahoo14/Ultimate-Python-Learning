# Write a python program using function to convert Celsius to Fahrenheit

# function to calculate fahrengeit to celsius
def f_to_c(f):
    return (5 * (f - 32)/9)

f = int(input("Enter The Fahrenheit Value: "))
print(round(f_to_c(f), 2))