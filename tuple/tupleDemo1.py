# data = ()
# print(data)
# print(type(data))

data =("amit","sumit","raj","parth")
#print(data[0])

#range
# for i in range(0,len(data)):
#     print(data[i])

#foreach
# for i in data:
#     print(i)

#immutable:
#data[0] ="AMITA" #TypeError: 'tuple' object does not support item assignment
print(data)

cnt = data.count("raj")
print("count = ",cnt)

ind = data.index("sumit")
print(ind)
