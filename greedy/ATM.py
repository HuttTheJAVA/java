import sys
input = sys.stdin.readline
n = int(input())

my_turn = []


minutes = list(map(int,input().split()))

minutes.sort()

for i in range(n):
    my_turn.append(sum(minutes[:i+1]))

print(sum(my_turn))