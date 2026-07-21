data = {"a":"raj","b":"parth","c":"jay","d":"neha"}
print(data)

#pop
# data.pop("ca")
# print(data)

r = "c"
#soln

if r in data:
    removedELm = data.pop(r)
    print(f"removing {removedELm}")
else:
    print(f" {r} key is not present to remove !")    

print(data)


#remove last key value pair and return also
removedELm = data.popitem()
print("remving..",removedELm)
print(data)
