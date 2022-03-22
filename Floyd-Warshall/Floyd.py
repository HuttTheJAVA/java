import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())

e = int(input())

matrix = [[INF]*n for i in range(n)]

for i in range(e):
    a,b,c = map(int,input().split())
    matrix[a-1][b-1] = min(matrix[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(n):
    matrix[i][i] = INF

for i in range(n):
    for j in range(n):
        if matrix[i][j] == INF:
            print(0,end=" ")
        else:
            print(matrix[i][j],end=" ")
    print()