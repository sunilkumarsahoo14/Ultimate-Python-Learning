# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter values in inchs: "))
print(f"{n}inch = {inch_to_cm(n)}cm")