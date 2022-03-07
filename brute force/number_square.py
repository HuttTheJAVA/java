import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = [list(map(int,input().strip())) for i in range(n)]

min_side = min(n,m)

max_square = 1

for i in range(1,min_side+1):
    for j in range(m-i):
        for k in range(n-i):
            if data[k][j] == data[k][j+i] == data[k+i][j] == data[k+i][j+i]:
                max_square = max(max_square,i+1)

print(max_square**2)