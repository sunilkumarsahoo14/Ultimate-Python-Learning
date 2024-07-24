# Write a program to find the greatest of four numbers entered by the user

n1 = int(input("Enter Number: "))
n2 = int(input("Enter Number: "))
n3 = int(input("Enter Number: "))
n4 = int(input("Enter Number: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("Greatest Number Is:", n1)

elif(n2>n1 and n2>n3 and n2>n4):
    print("Greatest Number Is:", n2)

elif(n3>n2 and n3>n1 and n3>n4):
    print("Greatest Number Is:", n3)
else:
    print("Greatest Number Is:", n4)