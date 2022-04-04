import sys
from collections import deque
import math as m

input = sys.stdin.readline

n = int(input())

dp = [0]*11

ninth = 9

for i in range(1,11):
    dp[i] = ninth*i
    ninth*=10

leng = len(str(n))

left_hab = sum(dp[:leng])

minsu = '9'*(leng-1)

if minsu != '':
    right_hab = leng*(n-int(minsu))
else:
    right_hab = leng*(n)

print(left_hab+right_hab)