n = int(input())
integer_list = map(int, input().split())
for x in range(len(integer_list)):
    integer_list[x]=int(integer_list[x])
t=tuple(integer_list)
print(hash(t))