import sys

input = sys.stdin.readline
INF = (1e9)
sundapchai = 0
for i in range(10):
    n = int(input())
    if abs(100-sundapchai) >= abs(100-(sundapchai+n)):
        sundapchai = sundapchai+n
    else:
        break

print(sundapchai)