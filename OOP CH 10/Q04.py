# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator():
    def __init__(self, n):
        self.n = n
    
    def squar(self):
        print(f"The squar of {self.n} is: {self.n * self.n}")
        
    def cube(self):
        print(f"The cube of {self.n} is: {self.n * self.n * self.n}")
        
    def sqr(self):
        print(f"The cube of {self.n} is: {self.n ** 1/2}")
        
    @staticmethod
    
    def default():
        print("Hellow coders")
        
num= Calculator(4)
num.default()
num.squar()
num.cube()
num.sqr()

# print(num.squar)
        