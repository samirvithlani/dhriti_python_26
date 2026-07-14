employees = ["raj","amit","parth","kunal","raj","parth","neha"]

uniqueelm = []

#
for i in employees:
    #raj,amit,partm,kunal,raj
    #raj not in ue
    if i not in uniqueelm:
        uniqueelm.append(i)#raj
print(uniqueelm)        