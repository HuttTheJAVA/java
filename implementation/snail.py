import sys
input = sys.stdin.readline

n = int(input())

num = int(input())

def direct(idx):  # 방향을 바꿔주는 함수 return 인덱스
    if idx == 4:
        idx = 0
    return idx

val = n*n

matrix = [[-1]*(n) for j in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

idx = 0

x,y = 0,0

matrix[x][y] = val
x_y = []
if val == num:
    x_y = [x+1,y+1]
val -= 1
while(1):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0<=nx<n and 0<=ny<n:
        if matrix[nx][ny] != -1:
            idx = direct(idx+1)
        else:
            matrix[nx][ny] = val
            if val == num:
                x_y.append(nx+1)
                x_y.append(ny+1)
            val -= 1
            x,y = nx,ny
            if val == 0:
                break
    else:
        idx = direct(idx+1)

for lines in matrix:
    print(*lines)

print(*x_y)