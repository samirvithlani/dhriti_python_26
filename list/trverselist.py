#list slicing..
employees = ["raj","amit","parth","kunal","raj","parth","neha"]

print(employees[0])
print(employees[-1])
print(employees[:]) #0 end
print(employees[0:4])# 0 1 2 3
print(employees[3::]) #0 start end.
print(employees[:3]) #0 1 2

print(employees[0::2])# 0 2 4 6


numbers = [1,2,3,4,5,6]
k=2
#[5,6,1,2,3,4]
print(numbers[-k:])
print(numbers[:-k])

x = numbers[-k:] + numbers[:-k]
print(x)
