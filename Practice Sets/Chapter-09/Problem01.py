# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’

with open("poems.txt", "r") as f:
    text = f.read()

# find = text.find("twinkle")
# if(find == -1):                # Also can try the logic

if("twinkle" in text):
    print("Poem contains the word twinkle")
else:
    print("Poem not contains the word twinkle")


