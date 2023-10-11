X=int(input("Enter a Number:"))
flag=False   

if X > 1:
    for i in range(2,X):
        if (X % i)==0:
          flag=True
        else:
            break

if flag:
    print(X, "is not a prime number")
    print("The factors of",X,"are:")
    for i in range(1, X + 1):
       if X % i == 0:
           print(i)
else:
    print(X, "is a prime number")  

print(" ")
print("The evaluated result of the equation is:")
for x in range(-5,5):
    result=Y=((8*x**2) + 1)
    print(result)