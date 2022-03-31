import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst1 = []

for i in range(m):
    six,one = map(int,input().split())
    lst1.append((six,one))

lst_six = sorted(lst1,key=lambda x:(x[0],x[1]))
lst_one = sorted(lst1,key=lambda x:(x[1],x[0]))

only_one = lst_one[0][1]*n

mix_buy = min(lst_six[0][0]*(int(n/6)) + (n-6*int(n/6))*lst_one[0][1],lst_six[0][0]*(int(n/6)+1))

print(min(mix_buy,only_one))