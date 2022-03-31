from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

vals = list(map(int,input().split()))

lst = deque([i+1 for i in range(n)])

calc = 0

def Left(lst):
    global calc
    lst.append(lst.popleft())
    calc += 1


def Right(lst):
    global calc
    lst.appendleft(lst.pop())
    calc += 1

for val in vals:
    idx = lst.index(val)
    if lst[0] == val:
        lst.popleft()
        continue
    lst_left = idx
    lst_right = len(lst)-1-idx
    if lst_left <= lst_right:
        for _ in range(lst_left):
            Left(lst)
    else:
        for _ in range(lst_right+1):
            Right(lst)

    lst.popleft()
    

print(calc)