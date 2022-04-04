from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m,k = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

data = [[0]*m for i in range(n)]

visit = [[0]*m for i in range(n)]

for i in range(k):
    x,y = map(int,input().split())
    data[x-1][y-1] = 1

def dfs(x,y):
    qu = deque()
    qu.append((x,y))
    count = 0
    while qu:
        x,y = qu.popleft()
        if visit[x][y] == 1:
            continue
        visit[x][y] = 1
        count += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny] == 1:
                    qu.append((nx,ny))
    return count

max_food = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and visit[i][j] == 0:
            max_food = max(max_food,dfs(i,j))

print(max_food)