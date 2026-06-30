data = "india"
index = -1
c = input("enter char to check :")

for i in range(0,len(data)):
    if c == data[i]:
        index = i 
        break

print("index = ",index)   