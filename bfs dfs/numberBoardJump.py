import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

data = []

for i in range(5):
    data.append(list(input().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

results = []

def dfs(x,y,word):
    if len(word) == 6:
        if word not in results:
            results.append(word)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,word+data[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i,j,data[i][j])

print(len(results))