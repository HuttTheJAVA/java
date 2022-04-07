from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

data = []

for i in range(N):
    data.append(list(map(int,input().split())))

minus_zero_one = [0,0,0]

def cut(lst,N):
    global minus_zero_one
    if N == 1:
        minus_zero_one[lst[0][0]+1] += 1
        return

    if lst[0][0] == 0:
        result = True
        for line in lst:
            if line.count(0) != N:
                result = False
                break
        if result == True:
            minus_zero_one[1] += 1
            return
    
    elif lst[0][0] == 1:
        result = True
        for line in lst:
            if line.count(1) != N:
                result = False
                break
        if result == True:
            minus_zero_one[2] += 1
            return
        
    elif lst[0][0] == -1:
        result = True
        for line in lst:
            if line.count(-1) != N:
                result = False
                break
        if result == True:
            minus_zero_one[0] += 1
            return

    cutt = N//3
    g1 = [lst[i][:cutt] for i in range(cutt)]
    g2 = [lst[i][cutt:(2*cutt)] for i in range(cutt)]
    g3 = [lst[i][(2*cutt):] for i in range(cutt)]
    g4 = [lst[i][:cutt] for i in range(cutt,2*cutt)]
    g5 = [lst[i][cutt:(2*cutt)] for i in range(cutt,2*cutt)]
    g6 = [lst[i][(2*cutt):] for i in range(cutt,2*cutt)]
    g7 = [lst[i][:cutt] for i in range(2*cutt,N)]
    g8 = [lst[i][cutt:(2*cutt)] for i in range(2*cutt,N)]
    g9 = [lst[i][(2*cutt):] for i in range(2*cutt,N)]
    cut(g1,N//3)
    cut(g2,N//3)
    cut(g3,N//3)
    cut(g4,N//3)
    cut(g5,N//3)
    cut(g6,N//3)
    cut(g7,N//3)
    cut(g8,N//3)
    cut(g9,N//3)
    return

cut(data,N)

for i in minus_zero_one:
    print(i)