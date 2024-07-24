"""
1     --->   SNAKE
-1    --->   WATER
0     --->    GUN
"""

import random

print("Snake - Water - Gun\n")
computer = random.choice([-1, 0, 1])
youStr = input("Enter Your Choice: ")
if(youStr not in ["s", "w", "g"]):
    print("Please Enter Correct Input\n")

youDict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

print(f"Computer Choice: {reverse_dict[computer]}\nYour Choice: {reverse_dict[you]}")

if(computer == you):
    print("Game Draw!")
else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    else:
        print("Something Went Wrong!!!")


"""
### New things I learn from -> CodeWithHarry

Another formula for simplify the conditions:
if(computer - you) == -1  or (computer - you) == 2   ---> print("You Lose")
else ---> print("You Win")
"""