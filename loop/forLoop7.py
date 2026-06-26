'''
  * 
 * *
* * *      

'''
#i =1
#i =2
for i in range(1,4):
    #0, 3-2 ,0,1
    for j in range(0,3-i):
        print(" ",end=" ")
    
    for j in range(1,i+1):
        print("* ",end=" ")    
        
    print()    