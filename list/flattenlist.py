data = [1,[2,[3]]]
copydata = data
result =[]

#[1,[2,[3]]]
while copydata:
    #x = [1,[2,[3]]].pop()
    x = copydata.pop()
    #[2,[3]]
    #[3] == list
    if type(x)==list:
        #[1,[2,[3]]].[2,[3]]
        copydata.extend(x) #[2,[3]] #[3]
        print(copydata)
    else:
        result.append(x)    #[3,2,1]

print(result)
        