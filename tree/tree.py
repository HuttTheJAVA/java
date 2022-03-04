from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

group = [[] for i in range(n)]

has_parent = [0]*n

reaf_node_stair = -1

parent = None

for i in range(n):
    if n_lst[i] == -1:
        has_parent[i] = -1
        parent = i
        continue
    else:
        has_parent[i] = has_parent[n_lst[i]] + 1 #부모노드의 층계 +1
        reaf_node_stair = max(reaf_node_stair,has_parent[i])
    group[n_lst[i]].append(i)

del_node = int(input())

qu = deque()
qu.append(del_node)
if del_node != parent:
    group[n_lst[del_node]].remove(del_node)

while(qu):
    idx = qu.popleft()
    has_parent[idx] = -1
    for n_idx in group[idx]:
        if has_parent[n_idx]>=0:
            qu.append(n_idx)
    group[idx] = []

cnt = 0
if del_node != parent and not group[parent]:
    cnt += 1

for i in range(len(has_parent)):
    if has_parent[i] >= 0 and not len(group[i]):
        cnt += 1

print(cnt)