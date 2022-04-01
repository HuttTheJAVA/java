import sys
input = sys.stdin.readline
n,m = map(int,input().split())
matrix_1 = []
matrix_2 = []

for i in range(n):
    matrix_1.append(list(map(int,input().strip())))

for i in range(n):
    matrix_2.append(list(map(int,input().strip())))

def matrix(x,y):
    for i in range(3):
        for j in range(3):
            matrix_1[x+i][y+j] = abs(matrix_1[x+i][y+j]-1)

cnt = 0

for i in range((n-3)+1):
    for j in range((m-3)+1):
        if matrix_1[i][j] != matrix_2[i][j]:
            matrix(i,j)
            cnt += 1

cant = False

for i in range(n):
    if matrix_1[i] != matrix_2[i]:
        cant = True

if not cant:
    print(cnt)
else:
    print(-1)