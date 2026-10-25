def hello():
    print("Hellow world!")
    print("This is python Function.")
    
hello()

# sum of two numbers using function
def sum(a,b):
    return a+b
    
print("Sum=",sum(2,3))

# avg of two numbers

def avg(a,b,c):
    return (a+b+c)/2

print("Avg=",avg(2,3,4))

# Largest number

def large(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
        
print("Largest Number Is",large(40,20,30))