"""
n = int(input())
student_marks = {}
for x in range(n):
        name=str(input())
        score=int(input())
        student_marks[name]=score
        n=n-1
query_name=str(input())
"""
n=int(input())
class_list = dict()
for x in range (n):
 data = input('Enter name & score separated by ":" ')
 temp = data.split(':')
 class_list[temp[0]] = int(temp[1])
        