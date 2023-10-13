#Program to print binary,decimal,hexadecimal and octal numbers
n=int(input("Enter a number:"))
l1=len(bin(n)[2:])
for i in range(1,n+1):
     print(str(i).rjust(l1,' '),end=" ")
     print(oct(i)[2:].rjust(l1,' '),end=" ")
     print(hex(i)[2:].upper().rjust(l1,' '),end=" ")
     print(bin(i)[2:].rjust(l1,' '),end=" ")
     print("")