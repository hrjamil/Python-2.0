# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute?

class Change:
    a= 1
    
obj = Change()
obj.a=2
print(obj.a)