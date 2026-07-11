text = "python is programming"
print(text[0])
print(text[1:4]) #1 2 3
print(text[:4]) #0 1 2 3
print(text[:])
print(text[2:]) #2 to end

print(text[0::2]) #starts from 0 end --> incremnt by 2
print(text[::3])

text = "python"
#p  y  t  h  o  n
#0  1  2  3  4  5
#-5 -4 -3 -2  -1
print(text[-1])
print(text[-2])
print(text[::-1])