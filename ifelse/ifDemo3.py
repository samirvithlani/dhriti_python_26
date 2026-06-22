#nested if else 
#if
#  if

isJob = False
isVisa = True
#us green card

if isVisa == True:
    print("user has valid visa :")
    if isJob == True:
        print("user has job also")
        print("we can give green card :")
    else:
        print("user has no job green card can not proceed !!")    
else:
    print("user has no valid visa :")        
    
    

