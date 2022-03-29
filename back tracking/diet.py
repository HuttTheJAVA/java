import sys
input = sys.stdin.readline

n = int(input())

INF = sys.maxsize

ingredient = []

min_prot,min_fat,min_carbo,min_vita = map(int,input().split())

min_price = INF

min_order = []

for i in range(n):
    ingredient.append(list(map(int,input().split())))

def find_best(idx,prot,fat,carbo,vita,price,ingredient,order):
    global min_price
    global n
    global min_order
    global min_prot
    global min_fat
    global min_carbo
    global min_vita
    if prot >= min_prot and fat >= min_fat and carbo >= min_carbo and vita >= min_vita:
        if price < min_price:
            min_order = order.copy()
            min_price = price
    for i in range(idx+1,n):
        if price + ingredient[i][-1] < min_price:
            order.append(i+1)
            find_best(i,prot+ingredient[i][0],fat+ingredient[i][1],carbo+ingredient[i][2],vita+ingredient[i][3],price+ingredient[i][4],ingredient,order)
            order.pop()

for i in range(n):
    find_best(i,ingredient[i][0],ingredient[i][1],ingredient[i][2],ingredient[i][3],ingredient[i][4],ingredient,[i+1])

if min_price != INF:
    print(min_price)
    print(*min_order)
else:
    print(-1)