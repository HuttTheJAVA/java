import sys
input = sys.stdin.readline

n = int(input())

nums = []

def decreasing_num(n):
    for i in range(10):
        if int(str(n)[-1])>i:
            nums.append(int(str(n)+str(i)))
            decreasing_num(int(str(n)+str(i)))
        else:
            return

for i in range(10):
    nums.append(i)
    decreasing_num(i)

nums.sort()
if len(nums)>n:
    print(nums[n])
else:
    print(-1)