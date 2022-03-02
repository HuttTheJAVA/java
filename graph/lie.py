from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

truth = list(map(int,input().split()))

truth = truth[1:]

partys = []

persons = [0]*(n+1)

cnt = 0

for i in truth:
    persons[i] = 1

for i in range(m):
    party = list(map(int,input().split()))
    partys.append(party[1:])

group = [[]for i in range(n+1)]

for party in partys:
    for i in range(len(party)-1):
        for j in range(i+1,len(party)):
            group[party[i]].append(party[j])
            group[party[j]].append(party[i])

qu = deque([])

for i in truth:
    qu.append(i)

while(qu):
    x = qu.popleft()
    for i in group[x]:
        if persons[i]:
            continue
        else:
            persons[i] = 1
            qu.append(i)

for party in partys:
    know = 0
    for i in party:
        know += persons[i]
        if know:
            break
    if not know:
        cnt += 1

print(cnt)