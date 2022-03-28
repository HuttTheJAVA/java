import sys
input = sys.stdin.readline

n1,n2 = map(int,input().split())

def gcd(one,two):
    
    while(two != 0):
        one,two = two,one%two
    
    return one

def lcm(one,two):
    to = one
    t2 = two    
    min_gong = gcd(one,two)
    print(min_gong)
    min_time = min_gong*(to//min_gong)*(t2//min_gong)
    return min_time


print(lcm(n1,n2))