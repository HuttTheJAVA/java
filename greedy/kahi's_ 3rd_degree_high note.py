import sys
input = sys.stdin.readline

N,A,D = map(int,input().split())


octav = list(map(int,input().split()))

dp = [0]*(max(octav)+1)

for i in range(N):
    if octav[i] == A:
        dp[octav[i]] = 1
    elif octav[i]-D >= 1 and (octav[i]-A)%D == 0:
        if dp[octav[i]-D] == 1:
            dp[octav[i]] = 1

print(sum(dp))