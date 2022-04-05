import sys
input = sys.stdin.readline

leng = int(input())

switch = list(map(int,input().split()))

pop = int(input())

def one_to_zero(val):
    val = abs(val-1)
    return val

def girl_change(idx):
    right = leng - idx
    left = idx-1
    pivot = idx - 1
    switch[pivot] = one_to_zero(switch[pivot])
    area = min(left,right)
    for i in range(1,area+1):
        if switch[pivot-i] == switch[pivot+i]:
            switch[pivot-i] = one_to_zero(switch[pivot-i])
            switch[pivot+i] = one_to_zero(switch[pivot+i])
        else:
            break

def boy_change(idx):
    besu = idx
    idx = idx-1
    for i in range(idx,len(switch),besu):
        switch[i] = one_to_zero(switch[i])

order = []

for i in range(pop):
    a,b = map(int,input().split())
    order.append((a,b))

for i in order:
    if i[0] == 1:
        boy_change(i[1])
    else:
        girl_change(i[1])

for i in range(len(switch)):
    if i//20 and not i%20:
        print()
    print(switch[i],end=" ")
