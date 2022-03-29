from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

n_lst.sort()

n_lst = deque(n_lst)

min_val = 200001

while n_lst:
    num = n_lst.pop()+n_lst.popleft()
    min_val = min(min_val,num)

print(min_val)