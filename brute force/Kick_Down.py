from collections import deque
import sys
input = sys.stdin.readline

kick1 = list(map(int,input().strip()))

kick2 = list(map(int,input().strip()))

max_len = len(kick1)+len(kick2)

if len(kick1)<=len(kick2):
    s_kick = kick1
    b_kick = kick2
else:
    s_kick = kick2
    b_kick = kick1

for idx in range(len(b_kick)):
    res = True
    if idx+len(s_kick)<len(b_kick):
        for j in range(idx,idx+len(s_kick)):
            if (s_kick[j-idx]==2 and b_kick[j]==2) and s_kick[j-idx] == b_kick[j]:
                res = False
                break
        if res:
            max_len = min(max_len,len(b_kick))
    else:
        for j in range(idx,len(b_kick)):
            if (s_kick[j-idx]==2 and b_kick[j]==2) and s_kick[j-idx] == b_kick[j]:
                res = False
                break
        if res:
            max_len = min(max_len,idx+len(s_kick))
# 왼쪽으로 이동도 고려해야함.

for i in range(len(s_kick)):
    res = True
    for j in range(i,len(s_kick)):
        if (s_kick[j]==2 and b_kick[j-i]==2) and s_kick[j] == b_kick[j-i]:
            res = False
            break
    if res:
        max_len = min(max_len,i+len(b_kick))
    
print(max_len)