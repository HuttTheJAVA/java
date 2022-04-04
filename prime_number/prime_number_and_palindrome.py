import sys

input = sys.stdin.readline

n = int(input())

n_lst = [None]*1003002

for i in range(2):
    n_lst[i] = False

for i in range(len(n_lst)):
    if str(i) == str(i)[::-1] and n_lst[i] == None:
        res = True
        for j in range(2,int(i**0.5)+1):
            if not i%j:
                res = False
                break
        if res:
            n_lst[i] = "sosu_Fell"

for i in range(n,len(n_lst)):
    if n_lst[i] == "sosu_Fell":
        print(i)
        break