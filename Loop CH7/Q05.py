# 5. Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter a natural number:"))
i=1
sum=0

while i<(n+1):
    sum= i+sum
    i+=1
    
print(f"Sum of {n} sumbers is {sum}")