for t in range(1, int(input())+1):
    N = int(input())
    cnt = 1
    res = False
    for a in range(1,10):
        for b in range(1,10):
            if N==a*b:
                cnt+=1
                res = True
                break
        if res:
            break
    if cnt>1:
        print(f'#{t} Yes')
    else :
        print(f'#{t} No')