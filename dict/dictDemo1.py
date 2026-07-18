#empty dict

# data ={}
# print(data)
# print(type(data))


data = {"guj":"gandhinagar","mah":"mumbai","guj":"ahmedabad"}

#key 

print(data["guj"]) #if key is not present it wil throw error
print(data.get("maha"))#if key is not present it wil return None

#loop

# get all keys 
k = data.keys()
print(k)
v = data.values()
print(v)

kv = data.items()
print(kv)

for i,j in data.items():
    print(f"{i} - {j}")
