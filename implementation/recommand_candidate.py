import sys
input = sys.stdin.readline

n = int(input())

cnt = int(input())

history = list(map(int,input().split())) # 사진틀에 게재된 순서 이값의 dict가 0이면 제거 된것

photo_frame = [] # 요소가 n개 이상 들어올 수 없음. 조건문 잘 쓸것

dct = {}

INF = sys.maxsize

min_val = INF

for j in history:
    dct[j] = 0

for i in history:
    if i not in photo_frame:
        if len(photo_frame)>=n:
            for j in range(len(photo_frame)):
                if dct[photo_frame[j]] == min_val and dct[photo_frame[j]] != 0:
                    dct[photo_frame[j]] = 0
                    del photo_frame[j]
                    break
        dct[i] += 1
        min_val = dct[i]
        photo_frame.append(i)
    else:
        dct[i] += 1
        min_val = INF
        for k in dct:
            if dct[k]!= 0 and dct[k] < min_val:
                min_val = dct[k]

photo_frame.sort()
print(*photo_frame)