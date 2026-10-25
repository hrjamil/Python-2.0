print("break")
for i in range(11):
    if (i==5):
        break
    print(i)
    
print("continue")
for i in range(11):
    if (i%2!=0):
        continue
    print(i)