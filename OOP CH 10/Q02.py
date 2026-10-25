# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator():
    def __init__(self, n):
        self.n = n
    
    def squar(self):
        print(f"The squar of {self.n} is: {self.n * self.n}")
        
    def cube(self):
        print(f"The cube of {self.n} is: {self.n * self.n * self.n}")
        
    def sqr(self):
        print(f"The cube of {self.n} is: {self.n ** 1/2}")
        
num= Calculator(4)
num.squar()
num.cube()
num.sqr()

# print(num.squar)
        