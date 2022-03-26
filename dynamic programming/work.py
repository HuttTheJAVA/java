import sys
input = sys.stdin.readline

n = int(input())

group = [[] for i in range(n)]

dp = [0]*n

for i in range(n):
    info = list(map(int,input().split()))
    if info[1]>0:
        for todo in info[2:]:
            group[i].append(todo-1)
        time = 0
        for todo in group[i]:
            if dp[todo]>time:
                time = dp[todo]
        dp[i] = info[0]+time
    else:
        dp[i] = info[0]

print(max(dp))