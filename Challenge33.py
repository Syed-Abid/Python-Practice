import math
from collections import Counter
X=int(input("Enter the number of shoes:"))
size_list=Counter(map(int,input("Enter show size seperated by space:").split()))
total=[]
N=int(input("Enter the number of customers:"))
for i in range(N):
    a,b=(map(int,input("Enter shoe size and the amount paid:").split()))
    if size_list[a] > 0:
        total.append(b)
        size_list.subtract(Counter([a]))
print(sum(total))
