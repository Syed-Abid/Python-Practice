from audioop import avg
import math
N=int(input("Number of students:"))
X=int(input("Number of subjects:"))
for i in range(N):
    for j in range(X):
        marks=int(input("Enter the marks:"))
    avg=marks/X
    print("Average:","{:.1f}".format(avg))
    print("\n")