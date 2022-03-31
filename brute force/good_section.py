import sys

input = sys.stdin.readline
n = int(sys.stdin.readline())
arr = list(map(int,input().split()))

num1 = int(input())
cnt = 0
for i in range(1,max(arr)-1):
    result = True
    for j in range(i+1,max(arr)):
        for val in arr:
            if i<=val<=j:
                result = False
                break
        if result == False:
            break
        elif i<=num1<=j:
            cnt += 1
print(cnt)