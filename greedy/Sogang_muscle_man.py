import sys
input = sys.stdin.readline

n = int(input())

lose_muscle = list(map(int,input().split()))

lose_muscle.sort()

max_lose = -1

if len(lose_muscle)%2:
    max_lose = lose_muscle[-1]
    max_idx = len(lose_muscle)-2
    for i in range((len(lose_muscle)-1)//2):
        max_lose = max(max_lose,lose_muscle[i]+lose_muscle[max_idx-i])
else:
    max_idx = len(lose_muscle)-1
    for i in range(len(lose_muscle)//2):
        max_lose = max(max_lose,lose_muscle[i]+lose_muscle[max_idx-i])

print(max_lose)