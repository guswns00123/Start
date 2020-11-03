import sys
num = int(sys.stdin.readline())
a = [0 for i in range(301)]
for i in range(num):
    a[i] = int(input())


sum = [0 for i in range(301)]

sum[0] = a[0]
sum[1] = a[0] + a[1]
sum[2] = max(a[1]+a[2], a[0] + a[2])

for i in range(3,num):
    sum[i] = max(sum[i-3] + a[i-1]+ a[i], sum[i-2]+a[i])


print(sum[num-1])
