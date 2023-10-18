from itertools import product
A=list(map(int,input("Enter the list numbers seperated by space:").strip().split()))
B=list(map(int,input("Enter the list numbers seperated by space:").strip().split()))
C=list(map(int,input("Enter the list numbers seperated by space:").strip().split()))
print(list(product(A,B,C)))
