result = [["raj",21,22],["jay",23,21],["parth",23,23],["priya",20,24],["neha",25,16]]
print(result)

# for i in result:
#     for j in i:
#         print(j,end=" ")
#     print() #\n    

#append..
#result total = [43,44,41,..]    

sum=0
total =[]
for i in range(0,len(result)):
    sum = sum+(result[i][1] + result[i][2])
    total.append(sum)
    sum=0    
        
max =total[0]

for i in total:
    if i>max:
        max = i
print(max)  #max       
print(total)    
#44 -->index
ind = total.index(max) #44 -->index
#print(ind)
#find name from main list of ind
print("topper",result[ind][0])
    


#total -->list append --> 
#total index -->main list -->index ---> name.


data =[1,[2,[3]]]
print(data[0])
print(data[1])
print(data[1][1][0])

#[1,2,3]
#typeof ..

 