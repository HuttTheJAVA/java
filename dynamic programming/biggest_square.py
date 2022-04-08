import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = []

dx = [-1,-1,0]
dy = [0,-1,-1]

for i in range(n):
    data.append(list(map(int,input().strip())))


for i in range(1,n):
    for j in range(1,m):
        val = []
        if data[i][j] == 1:
            min_val = 100000
            for k in range(3):
                nx = i + dx[k]
                ny = j + dy[k]
                result = True
                if 0<=nx<n and 0<=ny<m:
                    min_val = min(min_val,data[nx][ny])
            data[i][j] = min_val+1
            

max_val = 0

for i in range(n):
    if max(data[i])>max_val:
        max_val = max(data[i])

if max_val:
    print((max_val)**2)
else:
    print(max_val)