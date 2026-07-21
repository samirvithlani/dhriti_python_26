result = {"raj":[78,67,90],"parth":[67,89,93],"jay":[90,92,88]}
print(result)
sum=0
for i,j in result.items():
    print(i)
    for m in j:
        print(m,end=" ")
        sum = sum+m
    print(f"total of {i} = {sum}")    
    sum=0
    print()    