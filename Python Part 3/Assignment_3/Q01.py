
s = (input("Enter a word:"))

s2= s[::-1]

print(s)
print(s2)

if s==s2:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")