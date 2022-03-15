import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*1001

val = [1,1,1,1,1,1,1,1,1,1]

hab = 0

for i in range(n):
    
    hab = sum(val)
    tmp = hab
    new_val = [0]*len(val)

    for j in range(1,len(val)):
        org_val = val[j-1]
        new_val[j] = hab-org_val
        hab -= org_val

    new_val[0] = tmp
    val = new_val

print(val[0]%10007)