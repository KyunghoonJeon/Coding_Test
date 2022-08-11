import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
num_list=list(map(int,input().split()))
num_list.sort(reverse=True)
res=0
first=num_list[0];second=num_list[1]
cnt_first=(m//k)*k;cnt_sec=m-cnt_first
res=cnt_first*first+cnt_sec*second
print(res)