# baekjoon problem number 20937

import sys
input = sys.stdin.readline


n = int(input())

n_lst = list(map(int,input().split()))

dct = {}

for i in range(n):
    if n_lst[i] in dct:
        dct[n_lst[i]] += 1
    else:
        dct[n_lst[i]] = 1

print(max(dct.values()))