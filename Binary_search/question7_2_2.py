# 계수 정렬을 활용한 풀이

import sys
input=sys.stdin.readline
n=int(input())
array=[0]*1000001

for i in input().split():
    array[int(i)]=1
m=int(input())
x=list(map(int,input().split()))

for i in x:
    if array[i]==1:
        print('yes',end=' ')
    else:
        print('no',end=' ')