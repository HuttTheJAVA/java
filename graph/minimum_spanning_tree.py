import sys
from collections import deque

input = sys.stdin.readline

def find_parent(num):
    if num != parent[num]:
        parent[num] = find_parent(parent[num])
    return parent[num]

def union(num1,num2):
    num1 = find_parent(num1)
    num2 = find_parent(num2)
    if num1<num2:
        parent[num2] = num1
    else:
        parent[num1] = num2

flight = 0
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
edge = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

edge.sort()

edge = deque(edge)

for _ in range(M):
    c,a,b = edge.popleft()
    if find_parent(a) != find_parent(b):
        union(a,b)
        flight += c

print(flight)