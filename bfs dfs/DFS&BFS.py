import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())

data = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    s,e =  map(int,input().split())
    data[s][e] = 1
    data[e][s] = 1

dfs_lst = []
bfs_lst = []
def dfs(start):
    dfs_lst.append(start)
    for j in range(n+1):
        if data[start][j] == 1:
            if j not in dfs_lst:
                dfs(j)

def bfs(start):
    qu = deque()
    qu.append(start)
    bfs_lst.append(start)
    while qu:
        num = qu.popleft()

        for j in range(n+1):
            if data[num][j] == 1:
                if j not in bfs_lst:
                    qu.append(j)
                    bfs_lst.append(j)

dfs(v)
bfs(v)
for i in dfs_lst:
    print(i,end=" ")
print()
for j in bfs_lst:
    print(j,end=" ")