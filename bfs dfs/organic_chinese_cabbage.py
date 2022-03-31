import sys
from collections import deque

xt = [0,1,0,-1]
yt = [1,0,-1,0]
input = sys.stdin.readline
def check_side(x,y):

    qu = deque()
    qu.append((x,y))
    visit[x][y] = True

    while qu:
        x,y = qu.popleft()

        for i in range(4):
            nx = x+xt[i]
            ny = y+yt[i]
            if 0<= nx < m and 0<= ny < n:
                if data[nx][ny] == 1 and visit[nx][ny]==False:

                    visit[nx][ny] = True
                    qu.append((nx,ny))

T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())

    data = [[0]*(n) for i in range(m)]
    visit = [[False]*(n) for i in range(m)]


    worms = 0


    for _ in range(k):
        x,y = map(int,input().split())
        data[x][y] = 1

    for i in range(m):
        for j in range(n):
            if visit[i][j] == False and data[i][j]==1:
                worms += 1
                check_side(i,j)

    print(worms)