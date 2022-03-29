import sys
import math as m
input = sys.stdin.readline

money,year = map(int,input().split())

dp = [0]*(year+1)

require_y = [1,3,5]
year_profit = [1.05,1.2,1.35]

dp[0] = money

for i in range(1,year+1):
    for j in range(len(require_y)):
        if i-require_y[j]>=0:
            dp[i] = max(dp[i],m.floor(dp[i-require_y[j]]*year_profit[j]))

print(dp[-1])