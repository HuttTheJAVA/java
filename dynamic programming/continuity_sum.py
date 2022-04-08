import sys
import copy

input = sys.stdin.readline


n = int(input())

n_lst = list(map(int,input().split()))

hab_lst = copy.deepcopy(n_lst)

for i in range(1,len(n_lst)):
    if n_lst[i]>hab_lst[i-1]+n_lst[i]:
        hab_lst[i] = n_lst[i]
    else:
        hab_lst[i] = hab_lst[i-1]+n_lst[i]

print(max(hab_lst))