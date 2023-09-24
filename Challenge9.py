x=int(input ("enter the size of list"))
stu=[]
record=[]
for i in range(0,x):

    
    stu.append(input())
    stu.append(input())
    record.append(stu)
    stu = []

print(record)       

def solve(record):
   min_mark=float
   (min_mark) = min(x[1] for x in record)
   record = [x for x in record if x[1] > min_mark]
   min2_mark = min(x[1] for x in record)
   record = sorted([x[0] for x in record if x[1] == min2_mark])
   for x in record:
      print(x)

solve(record)
