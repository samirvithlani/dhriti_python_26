data = ["amit","sumit","raj","parth","amit"]
print(data)

#list mutable
#element
data.append("jay")  #last data add
print(data)
data.extend(["kunal","priya"])
print(data)

removedElem = data.pop() #it will remove last element
print("removing...",removedElem)
print(data)

removedElem = data.pop(3)
print("removing...",removedElem)
print(data)
