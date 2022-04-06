import sys
input = sys.stdin.readline

cnt,e,w,n,s = map(int,input().split())

dir = [e,w,n,s]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

done = []

chance = 0

def crazy_robot(x,y,move,per):
    global chance
    if move == cnt:
        chance += per
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if dir[i] and (nx,ny) not in done:
            done.append((nx,ny))
            crazy_robot(nx,ny,move+1,per*(dir[i]/100))
            done.pop()

done.append((0,0))
crazy_robot(0,0,0,1)
print(chance)