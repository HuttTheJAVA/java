import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())

INF = sys.maxsize

data = []

path = [[INF]*m for i in range(n)]

path[0][0] = 0

for i in range(n):
    data.append(list(map(int,list(input().strip()))))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

qu = deque()

qu.append((0,0))

while qu:
    x,y = qu.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not data[nx][ny]:
                if path[nx][ny]>path[x][y]:
                    path[nx][ny] = path[x][y]
                    qu.append((nx,ny))
            else:
                if path[nx][ny]>path[x][y] + 1:
                    path[nx][ny] = min(path[nx][ny],path[x][y]+1)
                    qu.append((nx,ny))

print(path[n-1][m-1])