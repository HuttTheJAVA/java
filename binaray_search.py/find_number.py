import sys

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int,input().split()))

m = int(input())
m_lst = list(map(int,input().split()))

n_lst.sort()

def binary_search(lst,num,left,right):
    mid = (left+right)//2
    
    if left>right:
        return

    if num == lst[mid]:
        return 1
    
    elif num > lst[mid]:
        return binary_search(lst,num,mid+1,right)

    elif num < lst[mid]:
        return binary_search(lst,num,left,mid-1)
    

for val in m_lst:
    if binary_search(n_lst,val,0,len(n_lst)-1):
        print(binary_search(n_lst,val,0,len(n_lst)-1))
    else:
        print(0)