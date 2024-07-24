# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.

# Does this change the class attribute? ---> Interview Level Question

class Demo:
    a = 4

o = Demo()
print(o.a) # ---> Print the class attribute bcz instance attribute is absent
o.a = 0    # No it does not change the class attribute, it just set a instance attribte
print(o.a) # ---> Instance attribute is present so it print it

# Class attribute remain same value
print(Demo.a)