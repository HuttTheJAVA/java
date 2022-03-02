import sys
input = sys.stdin.readline

n = int(input())

buildings = list(map(int,input().split()))

in_sight = [0]*n

for i in range(len(buildings)-1):
    gradient = None
    for j in range(i+1,len(buildings)):

        if gradient == None:
            gradient = (buildings[j]-buildings[i])/(j-i)
            in_sight[i] += 1
            in_sight[j] += 1

        elif gradient < (buildings[j]-buildings[i])/(j-i):
            gradient = (buildings[j]-buildings[i])/(j-i)
            in_sight[i] += 1
            in_sight[j] += 1

print(max(in_sight))