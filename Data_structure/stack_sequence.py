from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

n_lst = []

for i in range(n):
    n_lst.append(int(input()))

word = ''

stack = [0]

val = 1

idx = 0
res = True
while(1):
    if stack[-1] == n_lst[idx]:
        word += '-'
        idx += 1
        stack.pop()
        if idx == len(n_lst):
            break
    else:
        if stack[-1] > n_lst[idx]:
            res = False
            break
        stack.append(val)
        val += 1
        word += '+'

if res:
    for i in word:
        print(i)   
else:
    print('NO')