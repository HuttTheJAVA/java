import sys
input = sys.stdin.readline

a,b = map(int,input().split())

lst = [i for i in range(1,50) for j in range(i)]

print(sum(lst[a-1:b]))