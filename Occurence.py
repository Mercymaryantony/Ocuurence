s = input("Enter the string")
c =input("Enter the character")
l= len(s)
count = 0
for i in s:
    if i == c:
        count = count+1
print(count)
