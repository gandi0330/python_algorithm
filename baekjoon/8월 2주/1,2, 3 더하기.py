import sys

t = int(input())

d = [0] * 11
d[0] = 1
d[1] = 2
d[2] = 4

for _ in range(t):
    n = int(sys.stdin.readline())

    
    for i in range(3,n):
        if d[i] == 0 :
            d[i] = d[i-1]+d[i-2]+d[i-3]
    
    
    print(d[n-1])


