# Write a program using functions to find greatest of three numbers.

def greatestNum():
    a= int(input("Enter a:"))
    b= int(input("Enter b:"))
    c= int(input("Enter c:"))
    
    if (a>b and a>c):
        print(f"{a} is greatest number among {a},{b},{c}")
    elif(b>c and b>a):
        print(f"{b} is greatest number among {a},{b},{c}")
    else:
        print(f"{c} is greatest number among {a},{b},{c}")
        
greatestNum()