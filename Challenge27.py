#Program to make a Minion game
from itertools import count


s=str(input("Enter a string:").upper())
countk=0
counts=0
test_str=s
game=[]
vowels="AEIOU"
res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
for sub in res:
    flag=any(sub.startswith(ele) for ele in vowels)
    
    if flag:
        game.append(sub)
        countk+=1
    else:
        counts+=1
print("Words are:" + str(game))
if counts > countk:
        print("Stuart is the winner" + str(counts))
else:
        print("Kevin is the winner" + str(countk))

