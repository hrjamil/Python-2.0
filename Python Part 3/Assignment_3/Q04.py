tup = (1,2,3,4,5,6,7,8,9,10)

even=[]
odd=[]
    
for a in tup:
    if a%2 == 0:
        even.append(a)
    else:
        odd.append(a)
    
even=tuple(even)
odd=tuple(odd)
print(even)
print(odd)