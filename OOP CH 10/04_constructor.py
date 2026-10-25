class Name():
    
    def __init__(self, name, dept, salary ):
        self.name=name
        self.dept = dept
        self.salary= salary
    
    def good(self):
        print(f"Good morning, department is {self.dept} and salary is {self.salary}")
    
    @staticmethod
    def default():
        print("This is static methode.")
    
stu1 = Name("jamil", "cse", 13000)
stu1.good()
print(stu1.name, stu1.dept, stu1.salary)
