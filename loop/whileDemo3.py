no = 123 # 1 + 2 + 3

#123 -->3 
#123 % 10 = 3
#123 -->12 --> 123 // 10

#12 --->2
#12 % 10 = 2
#12 --->1 --> 12 //10

sum = 0
while no>0:
    rem = no % 10  #123 =3,2,1
    #    0 +3 =3
    #  3 + 2 = 5
    #  5 + 1 = 6 
    sum = sum + rem
    no = no //10

print("sum = ",sum)    

#twin no is sum and mul both are same of no -->
#123 --> 1 + 2+ 3 = 6 1 * 2 * 3 = 6
    



