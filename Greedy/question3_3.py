import sys
input=sys.stdin.readline
n,m=map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))
# min_list=[]
# for i in range(n):
#     min_list.append(min(arr[i]))
# print(max(min_list))

result=0
for i in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)
    result=max(result, min_value)
print(result)