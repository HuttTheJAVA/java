import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

estosteness = [i for i in range(2,n+1)]

dp = [0]*(1001)

for i in estosteness:
    dp[i] = 1

qu = deque()

qu.append(2)

order = []

while(sum(dp)!=0):
    num = qu.popleft()
    for i in range(num,n+1,num):
        if dp[i] == 1:
            dp[i] = 0
            order.append(i)
    for i in range(2,n+1):
        if dp[i] == 1:
            qu.append(i)
            break

print(order[m-1])