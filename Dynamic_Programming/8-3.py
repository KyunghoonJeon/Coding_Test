# 호출되는 함수 확인
dp=[0]*100

def pibo(x):
    print('f('+str(x)+')',end=' ')
    if x==1 or x==2:
        return 1
    if dp[x]!=0:
        return dp[x]
    dp[x]=pibo(x-1)+pibo(x-2)
    return dp[x]

pibo(6)