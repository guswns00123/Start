import sys
num = int(sys.stdin.readline())
arr =[]
for i in range(num):
    a = int(input())
    arr.append(a)

print(arr)
arr2 =[]
c = 0
for i in range(1,num):
    c-=1
    for j in range(i):
        if i == 1:
            arr2.append(0)

        else:
            arr2.append(arr[c])
            c+=1
            print(arr2)


print(arr2)
