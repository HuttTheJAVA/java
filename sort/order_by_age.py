import sys
input = sys.stdin.readline

n = int(input())

sign_in = []
for i in range(n):
    a,b = input().split()
    sign_in.append((int(a),b))

sign_in.sort(key=lambda x:x[0])

for i in sign_in:
    print(i[0],i[1])