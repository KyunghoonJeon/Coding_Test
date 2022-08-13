# 이진 탐색을 활용한 풀이

import sys
input=sys.stdin.readline
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n=int(input())
array=list(map(int,input().rstrip().split()))
m=int(input())
find=list(map(int,input().rstrip().split()))
array.sort()

for i in find:
    result=binary_search(array,i,0,n-1)
    if result!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')