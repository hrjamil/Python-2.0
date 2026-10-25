class Name():
    dept = "cse"
    sub= "python" # this is class attribute.
    courseCode= 403
    
    def good(self):
        print("Good morning")
    
    @staticmethod
    def default():
        print("This is static methode.")
    
stu1 = Name()
stu1.good()
stu1.default()
stu1.name = "Jamil" # This is instance attribute.
print(stu1.name, stu1.dept, stu1.sub, stu1.courseCode)
