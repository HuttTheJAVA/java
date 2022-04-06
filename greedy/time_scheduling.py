import sys
input = sys.stdin.readline

n = int(input())

time = []

min_val = sys.maxsize

for i in range(n):
    a,b = map(int,input().split())
    time.append([a,b])

time.sort(key= lambda x:(x[1],x[0]))

for i in range(1,n):
    time[i][0] = time[i-1][0]+time[i][0]

cant = False

for i in range(n):
    if time[i][0]>time[i][1]:
        cant = True
        break
    min_val = min(min_val,time[i][1]-time[i][0])

if cant == True:
    print(-1)
else:
    print(min_val)