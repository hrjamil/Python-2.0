class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        
    def get_cgpa (self):
        return self.cgpa
        
stu1 = student("jamil", 3.28)
stu2 = student("rahman", 3.00)

print(stu1.name, stu1.get_cgpa())