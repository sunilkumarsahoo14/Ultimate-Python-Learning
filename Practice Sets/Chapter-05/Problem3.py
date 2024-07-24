# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()

n = input("Enter Data: ")
s.add(n)

n = input("Enter Data: ")
s.add(int(n))

print(s)