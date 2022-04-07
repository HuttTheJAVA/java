import sys
input = sys.stdin.readline

sosu,k = map(int,input().split())


def answer():
    for i in range(2,k):
        if sosu%i == 0:

            print(f"BAD {i}")
            return
    print("GOOD")

answer()