no = 1234567 #no of digit count...

#123 / 10 = 12 ->no =12 count =1
#12  /10 =  1  -->no =1 count =2
#1 /10   =  0 --> no =0 count =3

#no = 4589
#4589 / 10 = 458 -- >count =1
#458 / 10 = 45 --> count 2
#45 /10 = 4  --> count 3
#4 / 10 = 0 -> count 4

count=0
while no>0:
    no = no // 10
    
    count+=1

print("count = ",count)    