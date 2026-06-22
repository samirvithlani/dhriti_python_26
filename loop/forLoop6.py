'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''
#i=1,i=2,i=3
k=0
for i in range(1,6):
    #j=1,j=1,j=2,j=1,j=2,j-3
    #k=1,k=2,k=3,k=4,k=5,k=6
    for j in range(1,i+1):
        k+=1
        print(k,end=" ")
    print()    