import sys
input= sys.stdin.readline


dp = [0]*251

dp[0] = 1
dp[1] = 1
dp[2] = 3
while(1):
    try:
        n = int(input())

        for i in range(3,n+1):
            dp[i] = dp[i-1]+2*dp[i-2]
            
        print(dp[n])
    except:
        break