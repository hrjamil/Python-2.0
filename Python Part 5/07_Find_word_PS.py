data = True
line = 1
word= "python"
with open("sample.txt", "r") as f:
    
    while data:
        data = f.readline()
        
        if (word in data):
            print(f"The word {word} is found at line {line}.")
            break
        # print(data)
        line +=1
    