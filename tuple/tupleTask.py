players = ["amit","sumit","raj","parth","jay","ajay","neha","sumita","krishna","arjun"]

captain1 =[]
captain2 =[]
print("welcome to choose team")
print("welcome captain 1:")

print("press positions to select player max 5")
print(players)
for i in range(1,6):
    pos = int(input("enter pos:"))
    ind = (pos-1)
    captain1.append(players[ind])
    players.pop(ind)

print(captain1)    
captain2 = players
print(captain2)
        
        
    
    

