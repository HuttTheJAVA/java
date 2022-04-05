from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

customer = []

profit = []

for i in range(m):
    customer.append(int(input()))

customer.sort(reverse=True)

for i in range(min(n,m)):
    profit.append(customer[i]*(i+1))

print(customer[profit.index(max(profit))], max(profit))