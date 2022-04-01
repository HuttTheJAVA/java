num = int(input())
han_su = 0
for i in range(1,num+1):
    numstr = str(i)
    if len(numstr) <= 2:
        han_su += 1
        continue
    
    chimcha = int(numstr[0])-int(numstr[1])
    result = True
    for i in range(1,len(numstr)-1):
        cha = int(numstr[i])-int(numstr[i+1])
        if cha != chimcha:
            result = False
    if result == False:
        continue
    else:
        han_su += 1

print(han_su)