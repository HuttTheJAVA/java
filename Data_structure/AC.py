from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    commands = input().strip()
    n = int(input())
    lst = input().strip()
    if lst != '[]':
        n_lst = list(lst[1:-1].split(','))
    else:
        n_lst = []
    n_lst = deque(n_lst)
    rev = False
    res = True
    for command in commands:
        if command == 'D':
            if n_lst:
                if rev:
                    n_lst.pop()
                else:
                    n_lst.popleft()
            else:
                res = False
                break
        else:
            if rev:
                rev = False
            else:
                rev = True
    n_lst = list(n_lst)
    if res:
        if rev:
            print('['+','.join(n_lst[::-1])+']')
        else:
            print('['+','.join(n_lst)+']')
    else:
        print("error")