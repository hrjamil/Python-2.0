
f= open("TextFile.txt", "a+")
f.write("\nThis is append")
data= f.read()
print(data)
f.close()