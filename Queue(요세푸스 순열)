import sys
from collections import deque


a,b = map(int,sys.stdin.readline().split())

arr = []
res = deque([])
result = []
for i in range(a):
    res.append(i+1)


while res:
    for i in range(b-1):
        res.append(res[0])
        res.popleft()

    result.append(res.popleft())

    
    

print(end = "<")
for i in range(1, len(result)):
    print(result[i-1], end = ", ")


print(result[len(result)-1], end = ">")
