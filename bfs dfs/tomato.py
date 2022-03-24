from collections import deque
import sys

input = sys.stdin.readline

m,n = map(int,input().split())

data = []

xt = [0,1,0,-1]
yt = [1,0,-1,0]

for i in range(n):
    data.append(list(map(int,input().split())))

qu = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            qu.append((i,j))

while(qu):
    x,y = qu.popleft()
    for i in range(4):
        nx = x + xt[i]
        ny = y + yt[i]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if data[nx][ny] == 0:
            data[nx][ny] = data[x][y]+1
            qu.append((nx,ny))

maxday = 0

result = True

for line in data:
    if line.count(0) != 0:
        print(-1)
        result = False
        break
    if max(line)>maxday:
        maxday = max(line)

if result == True:
    print(maxday-1)