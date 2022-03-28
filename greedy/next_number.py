import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = list(map(int,input().strip()))
    result = False
    for i in range(len(num)-2,-1,-1):
        if num[i]<num[i+1]:
            pivot = i
            result = True
            break
    if result == True:
        resource = num[pivot+1:]
        resource.sort()
        for i in range(len(resource)):
            if resource[i]>num[pivot]:
                num[pivot],resource[i]=resource[i],num[pivot]
                break
        new_num = num[:pivot+1]+resource

    if result:
        for num in new_num:
            print(num,end="")
        print()
    else:
        print('BIGGEST')