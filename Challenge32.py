from itertools import permutations
s=input()
ans=[]
perm=permutations(s,2)
for word in perm:
        ans.append("".join(word))
for i in sorted(ans):
        print(i)