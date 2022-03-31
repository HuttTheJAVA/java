import sys

input = sys.stdin.readline

shoutout_0 = [0]*41
shoutout_1 = [0]*41

d = [0]*41
def fibo_0(n):
    if shoutout_0[n] != 0:
        return shoutout_0[n]

    if n<0 or n==1:
        return

    elif n == 0:
        shoutout_0[n] += 1
        return
    
    fibo_0(n-1)
    fibo_0(n-2)

    shoutout_0[n] = shoutout_0[n-1]+shoutout_0[n-2]

def fibo_1(n):
    if shoutout_1[n] != 0:
        return shoutout_1[n]

    if n<0 or n==0:
        return

    elif n == 1:
        shoutout_1[n] += 1
        return

    fibo_1(n-1)
    fibo_1(n-2)

    shoutout_1[n] = shoutout_1[n-1]+shoutout_1[n-2]


times = int(input())

for i in range(times):
    num = int(input())
    fibo_0(num)
    fibo_1(num)
    print(shoutout_0[num],shoutout_1[num])