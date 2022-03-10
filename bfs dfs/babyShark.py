from collections import deque
import sys
input = sys.stdin.readline

def eat_fishes():
    n = int(input())

    mep = []

    x = None
    y = None

    for i in range(n):
        mep.append(list(map(int,input().split())))

    for i in range(n): # counting fishes and select my fish x,y location
        for j in range(n):
            if mep[i][j]:
                if mep[i][j] == 9:
                    x = i
                    y = j
                    mep[x][y] = 0

    is_visit = [[0]*n for i in range(n)] 

    dx = [-1,0,0,1]
    dy = [0,-1,1,0]

    qu = deque()
    qu.append((0,x,y))

    is_visit[x][y] = 1

    size = 2

    sec = 0

    eat_cnt = 0

    can_eat = [] # this is the list for the fishes that i can eat in my location

    while(1): # this while will be break if there is no fishes in can_eat list
        while(qu):
            dist,x,y = qu.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if not is_visit[nx][ny]:
                        if mep[nx][ny] <= size:
                            if mep[nx][ny] and mep[nx][ny] < size:
                                can_eat.append((dist+1,nx,ny))
                            qu.append((dist+1,nx,ny))
                            is_visit[nx][ny] = 1
        if can_eat:
            can_eat.sort(key=lambda x:(x[0],x[1],x[2])) # have to sort the can_eat list with three standards (1: distance, 2: highest_located(lowest x), 3:most_left(lowest y))
            dist,nx,ny = can_eat[0]
            sec += dist
            qu = deque([(0,nx,ny)])
            is_visit = [[0]*n for i in range(n)] # reboot visit matrix for a new start(because the location is changed.)
            is_visit[nx][ny] = 1 # check myfish location visit
            eat_cnt += 1 
            mep[nx][ny] = 0
            can_eat = []
            if eat_cnt == size: # if eat_cnt is equle my size plus my size
                size += 1
                eat_cnt = 0 
        else:
            break

    return sec

print(eat_fishes())