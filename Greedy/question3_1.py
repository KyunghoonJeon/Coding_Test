import sys
input=sys.stdin.readline
N=int(input())
coin=[500,100,50,10]
# coin_num=[]
# for i in coin:
#     q,N=divmod(N,i)
#     coin_num.append(q)
# print(sum(coin_num))

cnt=0
for i in coin:
    cnt+=N//i
    N%=i
print(cnt)
