import sys
input = sys.stdin.readline

n,s = map(int,input().split())

n_lst = list(map(int,input().split()))

cnt = 0

def partial_sequence(idx,hab):
    global s
    global cnt
    global n
    if hab == s:
        cnt += 1
    for i in range(idx+1,len(n_lst)):
        partial_sequence(i,hab+n_lst[i])

for i in range(n):
    partial_sequence(i,n_lst[i])

print(cnt)