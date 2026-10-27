# 5. Write a Class ‘Trainʼ which has methods to book a ticket, 
#   get status (no of seats) and 
#   get fare information of train running under Indian Railways.

class Train:
    gd="Good Morning!"
    
    def __init__(self, name, journey, train_no):
        self.name = name
        self.journey = journey
        self.train_no= train_no
        
    def status(self):
        print(f"Hi {self.name}, your destination is {self.journey}")
    
    def information(self):
        print(f"This train is under bd railway.")        
        
p1 = Train("jamil","Dhaka", 333)
print(p1.gd)
p1.status()
p1.information()

