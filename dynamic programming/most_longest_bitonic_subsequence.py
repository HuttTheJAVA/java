import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

L_dp = [0]*n
R_dp = [0]*n
max_dp = 0
for i in range(n):
    for j in range(i):
        if n_lst[i]>n_lst[j]:
            L_dp[i] = max(L_dp[i],L_dp[j]+1)

for r in range(n-1,-1,-1):
    for k in range(n-1,r,-1):
        if n_lst[r]>n_lst[k]:
            R_dp[r] = max(R_dp[r],R_dp[k]+1)

for i in range(n):
    if L_dp[i]+R_dp[i]+1 > max_dp:
        max_dp = L_dp[i]+R_dp[i]+1

print(max_dp)