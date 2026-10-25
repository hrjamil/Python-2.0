# 2. Write a python program using function to convert Celsius to Fahrenheit.

def temp():
    c = float(input("Enter celsious: "))
    
    f= ((c*9)/5)+32
    print(f"{c} in Fahrenheit is: {f}")
    
temp()