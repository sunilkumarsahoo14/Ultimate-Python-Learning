# Most Tricky Interview Questions 

"""
What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
"""

s = set()
s.add(20)
s.add(20.0) # if values are same then the data types are not matters in python
s.add('20')

print(len(s))
