# Write a program to find out the line number where python is present from ques 6.


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print("Yes, Python is present. Line no:", lineno)
        break
    lineno += 1
else:              # else aapka tabhi chalega ---> jab for loop aapka poora complete hua ho...
    print("Python is not present!")