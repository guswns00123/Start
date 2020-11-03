import sys
num =int(sys.stdin.readline())

def fib(n):
    f = [0] * (n+1)
    f[0] = 1
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n-1]


print(fib(num))


