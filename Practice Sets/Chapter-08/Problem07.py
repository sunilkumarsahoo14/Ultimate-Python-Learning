# Write a python function to remove a given word from a list ad strip it at the same time.

# ---> very good question for understanding the return a specific list

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Sunil", "Harry", "Subham", "il"]

print(rem(l, "il"))