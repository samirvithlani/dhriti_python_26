data = ["amit","sumit","raj","parth","amit"]
print(data)

data.append("jay") #add element at last index..
print(data)

data.extend(["kunal","priya"])
print(data)

# data.extend("neha")
# print(data)

#remove:

remvoedElm = data.pop() #it will remove from end.
print("removing...",remvoedElm)
print(data)


remvoedElm = data.pop(3)
print("removing...",remvoedElm)
print(data)

