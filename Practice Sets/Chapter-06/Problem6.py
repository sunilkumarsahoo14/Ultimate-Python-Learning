"""
Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 - 100 => E
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
"""

marks = int(input("Enter Your Marks: "))

if marks < 50:
    grade = "F"
elif marks < 61:
    grade = "D"
elif marks < 71:
    grade = "C"
elif marks < 81:
    grade = "B"
elif marks < 91:
    grade = "A"
else:
    grade = "E"

print("Your Grade Is:", grade)