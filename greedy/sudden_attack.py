import sys
import math as m
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

me = n_lst[0]

n_lst = sorted(n_lst[1:],reverse=True)


for i in range(len(n_lst)-1,-1,-1):
    if me > n_lst[i]:
        me += n_lst[i]
        n_lst.pop()


if n_lst:
    print('No')
else:
    print('Yes')