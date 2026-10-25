# Ask the user to enter two integers and one float. Convert them all to floats
# and print their average.

a= int(input("Enter 1st int num:"))
b= int(input("Enter 2nd int num:"))
c= float(input("Enter a float num:"))

d= float(a)
e= float (b)

avg= (d+e+c)/3

print(a, type(a))
print(d, type(d))
print("Average of 3 numbers:",avg)