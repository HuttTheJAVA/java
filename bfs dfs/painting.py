from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

m,n = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

data = []

def dfs(x,y):
    qu = deque()
    qu.append((x,y))
    paint = 0
    while qu:
        x,y = qu.popleft()
        if visit[x][y] == 1 or data[x][y] == 0:
            continue
        visit[x][y] = 1
        paint += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            qu.append((nx,ny))
    return paint

for i in range(m):
    data.append(list(map(int,input().split())))

visit = [[False]*n for i in range(m)]
count = 0
max_draw = 0
for i in range(m):
    for j in range(n):
        if visit[i][j] == False and data[i][j] == 1:
            max_draw = max(max_draw,dfs(i,j))
            count += 1

print(count)
print(max_draw)