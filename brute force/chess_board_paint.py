import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = []

for i in range(n):
    data.append(list(input().strip()))

min_count = 50**2+1
for sero in range(n-7):
    for garo in range(m-7):
        count_W = 0
        count_B = 0
        pivot_W = 'W'
        pivot_B = 'B'
        for i in range(sero,sero+8):
            for j in range(garo,garo+8):
                    if (i+j)%2 == (sero+garo)%2 and data[i][j] != pivot_W or (i+j)%2 != (sero+garo)%2 and data[i][j] == pivot_W:
                        count_W += 1
        for i in range(sero,sero+8):
            for j in range(garo,garo+8):
                    if (i+j)%2 == (sero+garo)%2 and data[i][j] != pivot_B or (i+j)%2 != (sero+garo)%2 and data[i][j] == pivot_B:
                        count_B += 1
        count = min(count_B,count_W)
        min_count = min(min_count,count)

print(min_count)
