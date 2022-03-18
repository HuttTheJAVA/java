import sys
input = sys.stdin.readline

while(1):
    try:
        n = int(input())
        num = '1'
        while(1):
            if int(num)%n == 0:
                print(len(num))
                break
            else:
                num = num+'1'
    except:
        break