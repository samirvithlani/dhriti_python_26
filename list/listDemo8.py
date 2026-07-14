#dhriti backup

data = ["raj","parth","raj","jay","neha","parth"]

#Index..
ind = data.index("jay")
print(ind)

cnt = data.count("parth")
print(cnt)


data.insert(1,"kunal")
#print("after...",data)


#data = ["raj","parth","raj","jay","neha","parth"]
#data.reverse()
#data.sort() #alph sort
#data.sort(reverse=True) #dsc sort
#print(data)

marks = [11,21,33,1,2,44,56,8]

#marks.sort()
marks.sort(reverse=True)
print(marks)
