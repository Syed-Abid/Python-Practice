list=[]
N = int(input())
for x in range(N):
  cmd=input().split()  
  if cmd[0] == "insert":
    list.insert(int(cmd[1]) , int(cmd[2]))
  
  elif cmd[0] == "print":
    print(list)
  
  elif cmd[0] == "remove":
    list.remove(int(cmd[1]))
  
  elif cmd[0] == "append":
    list.append(int(cmd[1]))
  
  elif cmd[0] == "sort":
    list.sort()
  
  elif cmd == "pop":
    list.pop()
  
  else:
    list.reverse()

  
