import sys
input = sys.stdin.readline

n,s = map(int,input().split())

n_lst = list(map(int,input().split()))

INF = sys.maxsize

start = 0
end = 0

hab = n_lst[end]

result = False

length = INF

while(start<=len(n_lst)-1):
    if hab >= s:
        length = min(length,end-start+1)
        if length == 1:
            break
        hab -= n_lst[start]
        start += 1
    elif hab < s:
        end += 1
        if end > len(n_lst)-1:
            break
        hab += n_lst[end]

if length == INF:
    print(0)
else:
    print(length)