# dp=[0]*100

# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     if dp[x]!=0:
#         return dp[x]
#     dp[x]=fibo(x-1)+fibo(x-2)
#     return dp[x]

# print(fibo(99))

dp=[0]*101
dp[1]=1;dp[2]=1
for i in range(3,101):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[99])