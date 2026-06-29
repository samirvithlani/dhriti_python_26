no1 = int(input("enter no 1"))
no2 = int(input("enter no 2"))

max =None #15
lcm = None
if no1>no2:
    max = no1
else:
    max = no2    

while True:
    #   15 % 10 == and 15 % 15 ==0 false
    if max % no1 == 0 and max % no2 ==0:
        lcm = max
        break
    max+=1   

print("lcm  = ",lcm)     
        
        
'''
    10,15 =30
    1 % 10 and 1 % 15 =false
    2,3,4,5,6,7,8,9,
    10 % 10 and 10 % 15 = false
    11,12,13,14,
    15 % 10 and 15 % 15 = false
    16,17,18,19,20,21,19,30
    30 % 10 and 30 % 15 true

'''
