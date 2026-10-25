# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer():
    companey = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
    def get(self):
        print("Good Morning")
        
p1 = Programmer("jamil", 13000, 2424)
p1.get()
print(p1.name, p1.salary, p1.pin)

p2 = Programmer("jahid", 12000, 2425)
print(p2.name, p2.salary, p2.pin)

p3 = Programmer("bob", 10000, 2426)
print(p3.name, p3.salary, p3.pin)

p4 = Programmer("jacl", 11000, 2427)
print(p4.name, p4.salary, p4.pin)
        