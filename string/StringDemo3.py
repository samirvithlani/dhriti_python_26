#copy

name= "naman"
copyaname = name
print(copyaname)

revName = ""

for i in range(len(name)-1,-1,-1):
    revName = revName + name[i]

print(revName)    

if name == revName:
    print("palindrome")
else:
    print("not plaindrome")    
    