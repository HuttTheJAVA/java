import sys
from collections import deque
input = sys.stdin.readline

depth,dow = map(int,input().split())

oven_d = list(map(int,input().split()))

for i in range(1,len(oven_d)):
    if oven_d[i-1]<oven_d[i]:
        oven_d[i] = oven_d[i-1]

dow_d = list(map(int,input().split()))
dow_d = deque(dow_d)

while(oven_d and dow_d):
    if oven_d[-1] >= dow_d[0]:
        dow_d.popleft()
        oven_d.pop()

    else:
        oven_d.pop()

if not(dow_d):
    print(len(oven_d)+1)
else:
    print(0)