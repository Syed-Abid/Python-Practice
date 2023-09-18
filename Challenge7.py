from itertools import permutations

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
n=int(input("Enter a number:"))

#new_list=(permutations([x,y,z]))
#l=[i for i in new_list if(x+y+z == n)]
#print(l) 

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))