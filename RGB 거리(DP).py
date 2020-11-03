import sys
num = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for i in range(num)]
for i in range(num-1):
    for j in range(i+1):
        if j == 0 :
            arr[i+1][j] = arr[i+1][j] + arr[i][j]
            print(arr[i][j])
        if j == i:
            arr[i+1][j+1] = arr[i+1][j+1] + arr[i][j]
            print(arr[i][j])
        else:
            arr[i+1][j+1] = max(arr[i][j]+arr[i+1][j+1], arr[i][j+1]+arr[i+1][j+1])
           


print(max(arr[num-1]))
