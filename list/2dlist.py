result = [["raj",21,22],["jay",23,21],["parth",18,23],["priya",20,24],["neha",25,16]]
print(result)

# for i in result:
#     for j in i:
#         print(j,end=" ")
#     print() #\n    

#append..
#result total = [43,44,41,..]    


for i in range(0,len(result)):
    #print(result[i])
    for j in range(0,len(result[i])):
        print(result[i][j],end=" ")
    print()    


#total -->list append --> 
#total index -->main list -->index ---> name.