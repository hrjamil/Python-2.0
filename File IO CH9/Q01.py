# f= open("poem.txt")
# c= f.read()
# print(c)

# if ("twinkle" in c):
#     print("The word twinkle is present in the file.")
# else:
#     print("The word twinkle is not present in the file.")
# f.close()

with open("poem.txt") as f:
    # print(f.read())
    c= f.read()
    print(c)
    if ("twinkle" in c):
        print("The word twinkle is present in the file.")
    else:
        print("The word twinkle is not present in the file.")