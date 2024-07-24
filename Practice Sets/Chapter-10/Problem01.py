# Create a class “Programmer” for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = Programmer("Sunil", 1200000, 759118)
print(p.name, p.company, p.salary, p.pin)

r = Programmer("Rohan", 1200000, 759118)
print(r.name, r.company, r.salary, r.pin)