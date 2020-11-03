import sys

num = int(sys.stdin.readline())
arr =[]
brr = []
for i in range(num):
    a, b = map(int, (sys.stdin.readline().split()))
    arr.append(a)
    brr.append(b)

dp = [0] * (num)
c= 0
for i in range(num):
    dp[i] = 1
    for j in range(num):
            if (arr[i] > arr[j] and brr[i] > brr[j] )or (arr[i] < arr[j] and brr[i] < brr[j]):
                dp[i] = max(dp[i],dp[j]+1)
                
                c = max(c,dp[i])


print(num-c)
