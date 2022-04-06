import sys
input = sys.stdin.readline

n,m = map(int,input().split())

INF = sys.maxsize

graph = [[INF]*n for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
                graph[j][i] = min(graph[i][j],graph[i][k] + graph[k][j])
min_idx = 0

min_val = INF

for i in range(n):
    if sum(graph[i])<min_val:
        min_idx = i
        min_val = sum(graph[i])

print(min_idx+1)