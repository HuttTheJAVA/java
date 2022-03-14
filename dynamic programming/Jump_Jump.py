import sys
input = sys.stdin.readline

INF = (1e9)

n = int(input())

jump = list(map(int,input().split()))

dp = [INF]*n

dp[0] = 0

for i in range(n):
    for j in range(i+1,i+jump[i]+1):
        if j<=n-1:
            dp[j] = min(dp[j],dp[i]+1)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])