#to find an unknown angle in a right angle triangle5
import math
AB=int(input("Enter the value of side:"))
BC=int(input("Enter the value of side:"))
#Now we are applying pythagoras theorem
H=math.sqrt(AB**2 + BC ** 2)
res=round(math.degrees(math.acos(BC/H)))
degree=chr(176)
print(res,degree,sep='') #sep is the separator used between multiple values when printing. The default is a space ( sep=' ' )