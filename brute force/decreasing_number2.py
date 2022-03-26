import sys
input = sys.stdin.readline

n = int(input())

decreasing_num = []

num = [0,1,2,3,4,5,6,7,8,9]

def make_decrease_num(number):
    global num
    global decreasing_num
    decreasing_num.append(int(number))
    for i in range(len(num)):
        if num[i]<int(number[-1]):
            number = number + str(num[i])
            make_decrease_num(number)
            number = number[:-1]

for i in range(len(num)):
    make_decrease_num(str(num[i]))

decreasing_num.sort()

if n-1<len(decreasing_num):
    print(decreasing_num[n-1])
else:
    print(-1)